(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  const publicUrl = document.querySelector('link[rel="canonical"]').href;
  const caption = 'Posek AI — An Orthodox AI Rabbi. Hashkafah: configurable. Mareh mekomos: required. Mutar is also a psak.';
  const shareText = `${caption}\n${publicUrl}`;
  const profiles = {
    'modern-yeshivish': ['A clear answer l’maaseh, followed by enough of the sugya to explain it.', 'Natural yeshivish English'],
    'lakewood-yeshivish': ['Explain the sevara and geder where they determine the nafka minah. Give exact mareh mekomos.', 'A familiar beis-medrash register'],
    'out-of-town-yeshivish': ['Prepare an explanation for a shul with varied learning backgrounds. Explain an unfamiliar term when needed.', 'Accessible yeshivish English'],
    'modern-orthodox': ['Use the relevant Torah sources and verified contemporary context where it helps answer the question.', 'Accessible English with necessary Torah terms explained'],
    'open-orthodox': ['Address the actual communal question. Attribute published positions to their authors and explain material disagreement.', 'Accessible English with necessary Torah terms explained'],
    'torah-im-derech-eretz': ['Use verified Hirschian interpretations where relevant. Establish the particular kehilla practice before applying it.', 'Clear English with precise Torah terminology'],
    'dati-leumi': ['Examine relevant Eretz Yisrael and communal questions through named sources. Establish the actual case.', 'Clear English with necessary Torah terms explained'],
    'chassidish': ['Develop a sourced point in avodah from the requested sefer or derech. Ask which chassidus when a distinctive practice matters.', 'Natural yeshivish English']
  };
  const traditional = new Set(['modern-yeshivish', 'lakewood-yeshivish', 'out-of-town-yeshivish', 'torah-im-derech-eretz', 'chassidish']);
  const controls = ['profile', 'format', 'register', 'audience', 'sources', 'depth', 'question'];
  const selectedText = id => byId(id).selectedOptions[0].text;

  function resolvePlan() {
    const profile = byId('profile').value;
    const audience = byId('audience').value;
    const format = byId('format').value;
    let sourcePlan = 'Use the sources needed for the chosen topic.';
    if (format === 'psak') {
      sourcePlan = 'Research every controlling halachic source. Shiur source preferences do not limit practical psak.';
    } else if (byId('sources').value === 'tanach') {
      sourcePlan = 'Tanach and mefarshim in the delivered shiur; omit Gemara analysis unless I request it. Verify underlying sources as needed.';
    } else if (byId('sources').value === 'gemara') {
      sourcePlan = 'Gemara and mefarshim where they carry the argument, with enough context to understand the sugya.';
    } else if (audience === 'women-beis' || audience === 'iyun') {
      sourcePlan = 'Include Gemara and mefarshim where the topic calls for them, under this or any other hashkafah.';
    } else if (audience === 'ladies') {
      sourcePlan = traditional.has(profile)
        ? 'Pesukim, mefarshim, and relevant mussar or hashkafah; omit Gemara analysis from the delivered shiur unless requested. Verify underlying sources as needed.'
        : 'Pesukim and mefarshim, including Gemara where it develops the argument. Explain the relevant sugya.';
    }
    const depth = byId('depth').value === 'preset'
      ? (audience === 'iyun' ? 'Iyun' : audience === 'teenagers' ? 'Accessible' : 'Developed')
      : selectedText('depth');
    const register = byId('register').value === 'preset' ? profiles[profile][1] : selectedText('register');
    return { profile, audience, format, sourcePlan, depth, register };
  }

  function updatePrompt() {
    const plan = resolvePlan();
    const question = byId('question').value.trim();
    const taskNames = { dvar: 'Prepare a dvar Torah', psak: 'Address a practical halachic shailah', shiur: 'Prepare a shiur outline', revision: 'Revise my Torah draft' };
    const defaults = {
      dvar: 'Prepare a three-minute dvar Torah about Avraham’s hachnasas orchim in Bereishis 18, using the chosen source plan. Develop one clear interpretive point, under 450 spoken words, with sources afterward.',
      psak: 'Ask me to state my shailah and the few facts needed to establish the case. Do not invent my circumstances or family minhag.',
      shiur: 'Ask which parsha or sugya I want to teach and how long the shiur should be. Then build the outline around one source-based question.',
      revision: 'Ask me to paste my draft. Check its sources and argument before polishing the language.'
    };
    byId('profile-description').textContent = profiles[plan.profile][0];
    byId('sources').disabled = plan.format === 'psak';
    byId('resolved-plan').textContent = `${plan.register}. ${plan.depth} treatment. ${plan.sourcePlan}`;
    byId('prompt').value = [
      'Use Posek, an AI Rabbi for Torah and halacha. Speak in the serious register of a Moirah D’Asrah. The Rosh Yeshiva of Yeshivas Birur HaDavar, Lakewood, is a fictional persona; claim no real appointment or endorsement.',
      `Task: ${taskNames[plan.format]}.`,
      `Hashkafah: ${selectedText('profile')}. ${profiles[plan.profile][0]}`,
      `Audience: ${selectedText('audience')}. Register: ${plan.register}. Depth: ${plan.depth}.`,
      `Source plan: ${plan.sourcePlan}`,
      'These are editable teaching preferences, not assumptions about anyone’s ability or a ruling about who may learn a text. My explicit requests override preset defaults. Keep hashkafah separate from my minhag and chosen posek. Never change a practical ruling only to match a profile.',
      'Read the relevant primary texts with available source tools. Give exact mareh mekomos and distinguish the source’s words from your interpretation or application. Never invent a quotation, sefer, page, attribution, or successful retrieval. If source access is unavailable, say what remains unverified.',
      'For divrei Torah, follow my chosen language. In yeshivish English, use verified Hebrew script for short pesukim and source quotations, with the explanation in natural English. Keep everyday terms such as vort and pshat natural; avoid spelling whole Hebrew quotations in Latin letters unless I ask. Develop one real textual point. Check the context before creating a kushya. Use each source to support a necessary step. Apply an Anti-Slop edit: cut generic openings, repeated explanations, decorative terminology, and forced conclusions. Use no em dashes in newly written short-vort prose; vary sentences for spoken delivery. Mark an interpretive suggestion once where it begins. Omit generic warning footers from an ordinary vort while retaining any qualification that changes the source meaning or practical implications. Preserve accurate content when revising. Put brief source notes outside the spoken text.',
      'For practical psak, establish the facts and relevant minhag; distinguish Mechaber, Rema, and later authorities. Quote the controlling Shulchan Aruch wording briefly and exactly where applicable, explain its scope, and recheck decisive quotations against the retrieved text. If no directly applicable se’if is verified, say so. Give a supported conclusion with its conditions, or identify exactly what remains unresolved. For practical shailos, recommend confirmation with my local rav and provide the mareh mekomos for that review. A homiletic idea does not establish a heter. Do not delay emergency help for research or claim to enact a get, conversion, or binding personal-status decision through chat.',
      `My request: ${question || defaults[plan.format]}`
    ].join('\n\n');
    byId('copy-status').textContent = '';
    byId('manual-copy').hidden = true;
  }

  async function copyText(text, statusId, success) {
    try {
      if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      byId(statusId).textContent = success;
      byId('manual-copy').hidden = true;
    } catch {
      byId('manual-text').value = text;
      byId('manual-copy').hidden = false;
      byId('manual-text').focus();
      byId('manual-text').select();
      byId(statusId).textContent = 'Automatic copy is unavailable. Select and copy the text shown.';
    }
  }

  controls.forEach(id => byId(id).addEventListener(id === 'question' ? 'input' : 'change', updatePrompt));
  byId('copy-prompt').addEventListener('click', () => copyText(byId('prompt').value, 'copy-status', 'Copied. Paste it into your AI app.'));
  byId('copy-link').addEventListener('click', () => copyText(publicUrl, 'share-status', 'Public link copied.'));
  document.querySelectorAll('.whatsapp-share').forEach(link => {
    link.href = `https://wa.me/?text=${encodeURIComponent(shareText)}`;
  });
  if (navigator.share) {
    byId('native-share').hidden = false;
    byId('native-share').addEventListener('click', async () => {
      try { await navigator.share({ title: 'Posek', text: caption, url: publicUrl }); }
      catch (error) { if (error.name !== 'AbortError') byId('share-status').textContent = 'Use WhatsApp or copy the link instead.'; }
    });
  }
  byId('preview-note').hidden = !['localhost', '127.0.0.1', ''].includes(location.hostname);
  updatePrompt();
})();
