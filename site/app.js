(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  const publicUrl = document.querySelector('link[rel="canonical"]').href;
  const skillGuideUrl = new URL('skill.html', publicUrl).href;
  const skillSourceUrl = 'https://github.com/frum-compatible/posek/blob/main/skills/posek/SKILL.md';
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
  let activeMode = document.querySelector('input[name="mode"]:checked').value;
  const modeFields = ['question', 'register', 'depth'];
  const drafts = {
    psak: { question: '', register: 'preset', depth: 'preset' },
    torah: { question: '', register: 'preset', depth: 'preset' }
  };
  const sampleQuestions = [
    {
      title: 'The Airbnb knife',
      question: 'We’re at an Airbnb with a regular nonkosher kitchen. I used a knife from its drawer to dice a raw onion on our own plastic cutting board, then mixed it through a tomato-and-cucumber salad. The knife was spotless, and nobody has used it during the two days we’ve been here. I don’t know what it cut before we arrived. Everything else was prepared with our own utensils, and the salad is in a disposable bowl. Can we eat it? Would picking out the onion help? Does our cutting board need kashering?'
    },
    {
      title: 'Coffee after tasting the cholent',
      question: 'Friday afternoon I tasted a teaspoon of gravy from our meat cholent to check the salt. It was liquid from the top, with no beans or meat in it, and I spat it into the sink without swallowing or chewing anything. I rinsed my mouth with water. I normally wait six hours after fleishigs, and I already made myself a coffee with milk. Did tasting the gravy start the six hours? Is rinsing enough before I drink the coffee? Would chewing a bean from the same pot and spitting it out be different?'
    },
    {
      title: 'Driving to the hospital on Shabbos',
      question: 'My wife is in labor on Shabbos, and the maternity team has told us to leave for the hospital immediately. Our car is outside. Someone told me that things for a yoledes should be done b’shinui when possible. Does that apply to unlocking my phone, starting the car, or the driving itself? I know pikuach nefesh overrides Shabbos; I’m asking where shinui still belongs and where attempting it would be wrong. Start with what we should do now, then explain the sources and the distinction between the actions.'
    },
    {
      title: 'Paying the Shabbos babysitter',
      question: 'We’re hiring a Jewish babysitter for Shabbos afternoon and paying on Sunday. To arrange havla’ah, we want to include ten paid minutes on Friday for her to meet the children and learn their routine, with one fee for both visits. Is that genuine weekday work or just a token addition? What if we agree that cancelling Friday would reduce her fee, but the Shabbos booking would still stand? Does one payment make this one job when either visit can be cancelled separately?'
    },
    {
      title: 'The airline “mezonos” roll',
      question: 'My kosher airline meal has a slightly sweet roll marked “mezonos.” I made mezonos and ate half with the chicken and potatoes before the person next to me said that using it for lunch makes it hamotzi. Do I stop now to wash and make a new bracha? Does the mezonos I already said cover anything, and what do I say afterward? Would eating the same roll by itself later change its status? Please separate the recipe question from being kovea seudah on it.'
    }
  ];

  function resolvePlan() {
    const profile = byId('profile').value;
    const format = document.querySelector('input[name="mode"]:checked').value === 'psak' ? 'psak' : byId('format').value;
    const audience = format === 'psak' ? 'general' : byId('audience').value;
    let sourcePlan = 'Use the sources needed for the chosen topic.';
    if (format === 'psak') {
      sourcePlan = 'Research every controlling halachic source needed for the question.';
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
      ? (format === 'psak' ? 'Concise' : audience === 'iyun' ? 'Iyun' : audience === 'teenagers' ? 'Accessible' : 'Developed')
      : selectedText('depth');
    const register = byId('register').value === 'preset' ? profiles[profile][1] : selectedText('register');
    return { profile, audience, format, sourcePlan, depth, register };
  }

  function updatePrompt() {
    const plan = resolvePlan();
    const [profileName, profileSubtitle] = selectedText('profile').split(' · ');
    byId('profile-name').textContent = profileName;
    byId('profile-subtitle').textContent = profileSubtitle;
    document.querySelectorAll('input[name="profile-choice"]').forEach(input => { input.checked = input.value === plan.profile; });
    const question = byId('question').value.trim();
    const taskNames = { dvar: 'Prepare a dvar Torah', psak: 'Address a practical halachic shailah', shiur: 'Prepare a shiur outline', revision: 'Revise my Torah draft' };
    const defaults = {
      dvar: 'Prepare a three-minute dvar Torah about Avraham’s hachnasas orchim in Bereishis 18, using the chosen source plan. Develop one clear interpretive point, under 450 spoken words, with sources afterward.',
      psak: 'Ask me to state my shailah and the few facts needed to establish the case. Do not invent my circumstances or family minhag.',
      shiur: 'Ask which parsha or sugya I want to teach and how long the shiur should be. Then build the outline around one source-based question.',
      revision: 'Ask me to paste my draft. Check its sources and argument before polishing the language.'
    };
    const questions = {
      psak: ['Your halacha question', 'For example: I forgot Yaaleh Veyavo in bentching on Rosh Chodesh. Do I repeat it?'],
      dvar: ['What should the dvar Torah be about?', 'For example: a three-minute vort on Yaakov’s pachim ketanim for the Shabbos table.'],
      shiur: ['What are you teaching?', 'For example: a 20-minute shiur on hachnasas orchim, with a source sheet.'],
      revision: ['Paste your draft', 'Paste your dvar Torah and say what you would like to improve.']
    };
    byId('prepare-title').textContent = plan.format === 'psak' ? 'Ask a shailah.' : 'Prepare a dvar Torah.';
    byId('question-label').textContent = questions[plan.format][0];
    byId('question').placeholder = questions[plan.format][1];
    byId('torah-settings').hidden = plan.format === 'psak';
    byId('sample-questions').hidden = plan.format !== 'psak';
    byId('rav-note').hidden = plan.format !== 'psak';
    byId('profile-description').textContent = profiles[plan.profile][0];
    byId('sources').disabled = plan.format === 'psak';
    byId('resolved-plan').textContent = `${plan.register}. ${plan.depth} treatment. ${plan.sourcePlan}`;
    byId('prompt').value = [
      `Read and apply the Posek skill:\n${skillSourceUrl}`,
      `Full instructions and reference guides:\n${skillGuideUrl}`,
      `Use web browsing to read the main skill, source-method, and hashkafah guides, then ${plan.format === 'psak' ? 'consequential-cases where relevant' : 'divrei-torah, torah-writing, and audience'}. Follow them when answering my request below. No installation is needed. If a link fails, try the other; if neither can be read, say so and ask me to paste the skill. Do not delay emergency care to read links.`,
      `Task: ${taskNames[plan.format]}.`,
      `Hashkafah: ${selectedText('profile')}.`,
      `Audience: ${plan.format === 'psak' ? 'General' : selectedText('audience')}. Register: ${plan.register}. Depth: ${plan.depth}.`,
      `Source plan: ${plan.sourcePlan}`,
      `My request: ${question || defaults[plan.format]}`
    ].join('\n\n');
    byId('copy-status').textContent = '';
    byId('manual-copy').hidden = true;
    byId('copied-app-links').hidden = true;
  }

  const profilePicker = byId('profile-picker');
  function closeProfilePicker() {
    profilePicker.open = false;
    byId('profile-trigger').focus();
  }
  [...byId('profile').options].forEach(option => {
    const [name, subtitle] = option.text.split(' · ');
    const label = document.createElement('label');
    const input = document.createElement('input');
    input.type = 'radio';
    input.name = 'profile-choice';
    input.value = option.value;
    input.className = 'sr-only';
    const text = document.createElement('span');
    text.className = 'profile-text';
    const title = document.createElement('span');
    title.className = 'profile-name';
    title.textContent = name;
    const detail = document.createElement('span');
    detail.className = 'profile-subtitle';
    detail.textContent = subtitle;
    text.append(title, detail);
    label.append(input, text);
    input.addEventListener('change', () => {
      byId('profile').value = input.value;
      byId('profile').dispatchEvent(new Event('change', { bubbles: true }));
    });
    input.addEventListener('click', event => { if (event.detail > 0) closeProfilePicker(); });
    byId('profile-options').append(label);
  });
  profilePicker.addEventListener('toggle', () => {
    if (profilePicker.open) profilePicker.querySelector('input:checked').focus();
  });
  profilePicker.addEventListener('keydown', event => {
    if (event.key === 'Escape' || (event.key === 'Enter' && event.target.matches('input'))) {
      event.preventDefault();
      closeProfilePicker();
    }
  });
  profilePicker.addEventListener('focusout', () => {
    setTimeout(() => {
      if (!profilePicker.contains(document.activeElement)) profilePicker.open = false;
    }, 0);
  });
  document.addEventListener('pointerdown', event => {
    if (!profilePicker.contains(event.target)) profilePicker.open = false;
  });
  byId('profile').hidden = true;
  profilePicker.hidden = false;

  let copying = false;
  const copyControls = document.querySelectorAll('[data-open-app], #copy-prompt, #copy-link');
  async function copyText(text, statusId, success) {
    if (copying) return false;
    copying = true;
    copyControls.forEach(control => { control.disabled = true; });
    byId('copied-app-links').hidden = true;
    try {
      if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      byId(statusId).textContent = success;
      byId('manual-copy').hidden = true;
      byId('copied-app-links').hidden = statusId !== 'copy-status' || text !== byId('prompt').value;
      return true;
    } catch {
      byId('manual-text').value = text;
      byId('manual-copy').hidden = false;
      byId('manual-app-links').hidden = statusId !== 'copy-status';
      byId('manual-text').focus();
      byId('manual-text').select();
      byId(statusId).textContent = 'Automatic copy is unavailable. Select and copy the text shown.';
      return false;
    } finally {
      copying = false;
      copyControls.forEach(control => { control.disabled = false; });
    }
  }

  sampleQuestions.forEach(sample => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'sample-question';
    button.textContent = sample.title;
    button.addEventListener('click', () => {
      byId('question').value = sample.question;
      byId('sample-questions').open = false;
      updatePrompt();
      byId('sample-questions').querySelector('summary').focus();
    });
    byId('sample-list').append(button);
  });

  controls.forEach(id => byId(id).addEventListener(id === 'question' ? 'input' : 'change', updatePrompt));
  document.querySelectorAll('input[name="mode"]').forEach(input => input.addEventListener('change', () => {
    modeFields.forEach(id => { drafts[activeMode][id] = byId(id).value; });
    activeMode = input.value;
    modeFields.forEach(id => { byId(id).value = drafts[activeMode][id]; });
    updatePrompt();
  }));
  const handoffButtons = document.querySelectorAll('[data-open-app]');
  handoffButtons.forEach(button => button.addEventListener('click', async () => {
    const copied = await copyText(byId('prompt').value, 'copy-status', `Copied. Opening ${button.dataset.appName}…`);
    if (copied) window.location.assign(button.dataset.openApp);
  }));
  byId('copy-prompt').addEventListener('click', () => copyText(byId('prompt').value, 'copy-status', 'Copied.'));
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
