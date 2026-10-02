# Publishing Posek

Publish the repository under the identity you intend readers to see. Keep authentication, commit attribution, and repository ownership separate in your setup. None of the steps below promises anonymity.

Finish reviewing the project first, then complete the personal-account login yourself. Publication follows only after the account, attribution, and public files have been checked.

## Choose a public identity

| Option | What readers can see |
| --- | --- |
| Existing personal account | The account owns the repository and is directly associated with it. |
| Project organization | A branded repository URL. Private organization membership does not hide commits, issues, pull requests, or releases made using your personal account. |
| Separate pseudonymous account | Better separation from an existing public identity, provided commits and public activity consistently use it. GitHub and the computer's administrator may still know who operates it. |

GitHub does not require a public real name, but its current Terms allow only **one free personal account per person**, with a separate exception for an account used exclusively for automation. Consider an appropriate paid account or ask GitHub Support before creating an additional personal account. A pseudonym must not impersonate a real person or institution. [Account terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service), [impersonation policy](https://docs.github.com/en/site-policy/acceptable-use-policies/github-impersonation)

An organization can hide public membership; this controls membership visibility, not every public action by its members. A GitHub noreply email protects your mailbox but normally contains your account username. Use the exact noreply address shown in the chosen publishing account's email settings. [Membership visibility](https://docs.github.com/en/account-and-profile/how-tos/organization-membership/publicizing-or-hiding-organization-membership), [noreply formats](https://docs.github.com/en/account-and-profile/reference/email-addresses-reference)

## Keep existing work configuration intact

Use a separate `GH_CONFIG_DIR` and HTTPS. Do not switch the active account in your usual GitHub CLI configuration, change global Git identity, or modify SSH configuration. Environment tokens override stored CLI logins, so the helper below removes them only for its subprocess. [CLI environment](https://cli.github.com/manual/gh_help_environment), [account switching](https://cli.github.com/manual/gh_auth_switch)

`GH_CONFIG_DIR` separates configuration files. It is **not a credential vault or a separate OS user**: the system keyring and browser remain shared, and credentials for the same GitHub account may be shared across configurations. Use a separate browser profile for the publishing identity and verify the account before every consequential action.

These are manual templates for a POSIX-style shell. Replace every `CHOOSE_…` value. Keep the CLI configuration directory outside the repository.

```sh
PUBLISHER='CHOOSE_LOGIN'
OWNER='CHOOSE_USER_OR_ORGANIZATION'
AUTHOR_NAME='CHOOSE_PUBLIC_AUTHOR_NAME'
AUTHOR_EMAIL='CHOOSE_EXACT_ACCOUNT_NOREPLY_EMAIL'

for value in "$PUBLISHER" "$OWNER" "$AUTHOR_NAME" "$AUTHOR_EMAIL"; do
  case "$value" in
    ''|CHOOSE_*) printf '%s\n' 'Stop: replace every identity placeholder.' >&2; exit 1 ;;
  esac
done

posek_gh_config="$HOME/.config/gh-posek"
mkdir -p "$posek_gh_config"
chmod 700 "$posek_gh_config"

posek_gh() {
  env -u GH_TOKEN -u GITHUB_TOKEN -u GH_HOST -u GH_REPO \
    GH_CONFIG_DIR="$posek_gh_config" gh "$@"
}

posek_gh auth login --hostname github.com --git-protocol https --web --scopes workflow
```

Complete browser authentication yourself. If asked **“Authenticate Git with your GitHub credentials?”**, answer **No**. Do not run `gh auth setup-git`; the push command below supplies its own helper. Login normally uses the system credential store but can fall back to plaintext if that store fails—review any warning. The `workflow` scope permits uploading the GitHub Actions workflow included in this repository. [Login](https://cli.github.com/manual/gh_auth_login), [credential setup](https://cli.github.com/manual/gh_auth_setup-git), [OAuth scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)

```sh
test "$(posek_gh api user --jq .login)" = "$PUBLISHER" || {
  printf '%s\n' 'Stop: authenticated account does not match PUBLISHER.' >&2
  exit 1
}
```

## Set attribution before committing

Run these inside the new, standalone Posek repository. First verify that you are in the intended project directory. An extracted release archive has no Git repository yet; initialize one there before configuring identity. If this is an existing checkout, inspect it rather than reinitializing it. These settings change only this repository. Git author names can be pseudonyms; email determines GitHub attribution. [Git author names](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git), [repository-specific email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)

For a fresh extracted copy, from its root:

```sh
git init -b main
```

For either a fresh copy or existing checkout, verify the root before setting identity:

```sh
test "$(git rev-parse --show-toplevel)" = "$(pwd -P)" || {
  printf '%s\n' 'Stop: Git root is not the current Posek directory.' >&2
  exit 1
}
```

```sh
git config --local user.name "$AUTHOR_NAME"
git config --local user.email "$AUTHOR_EMAIL"
git config --local user.useConfigOnly true

# Avoid inheriting a work signing identity in this personal repository.
git config --local commit.gpgSign false
git config --local tag.gpgSign false

git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

**Stop if either identity is wrong.** `GIT_AUTHOR_*` and `GIT_COMMITTER_*` environment variables can override configuration. Changing configuration does not repair previous commits. Review author and committer metadata, coauthor trailers, tags, screenshots, file contents, and local paths before publication. A clean source snapshot with correct attribution is easier to review than inherited history.

Stage only the intended project files and inspect the staged diff:

```sh
git add README.md LICENSE NOTICE CONTRIBUTING.md .gitignore \
  .github skills scripts tests benchmarks docs site
git diff --cached --stat
git diff --cached
```

Once the staged content and author identity are correct, make the initial commit and review it before pushing:

```sh
git commit -m 'Add Posek skill and development benchmark'
git show --no-patch --format=fuller HEAD
git status --short
```

## Create and push the public repository

The next command creates a **public** repository. Run it only after choosing the identity and reviewing the files. `OWNER` may be the authenticated user or an organization where that user can create repositories. An explicit owner prevents accidentally publishing under a default account. If `origin` already exists, inspect it instead of overwriting it. [Repository creation](https://cli.github.com/manual/gh_repo_create)

```sh
posek_gh repo create "$OWNER/posek" --public --source . --remote origin \
  --description 'An open-source Orthodox AI Rabbi and AI Posek for Torah, halacha, and divrei Torah. Source-based teshuvos, vortlach, and shiur preparation for Claude Code and Codex.'

git remote get-url --push origin
```

**Stop unless the effective push URL is `https://github.com/OWNER/posek` or that URL ending in `.git`, with your chosen owner substituted.** Existing Git URL rewrite rules can change the effective destination or protocol.

If a global rule rewrites GitHub HTTPS addresses to SSH, keep this personal repository on HTTPS with a more specific, repository-local rule, then inspect the effective URL again:

```sh
git config --local "url.https://github.com/$OWNER/.insteadOf" "https://github.com/$OWNER/"
git remote get-url --push origin
```

This does not change the global rewrite used by work repositories. A more specific inherited rule may still take precedence; the effective push URL must match before proceeding.

Assuming the reviewed branch is `main`:

```sh
env -u GH_TOKEN -u GITHUB_TOKEN -u GH_HOST -u GH_REPO \
  GH_CONFIG_DIR="$posek_gh_config" \
  git -c credential.helper= \
      -c 'credential.https://github.com.helper=!gh auth git-credential' \
      push --set-upstream origin main
```

The empty credential helper resets inherited helpers for this command; the next helper uses the separate CLI configuration. This does not install a global credential helper. Managed environments may also supply HTTP authentication settings; resolve those before pushing if the selected identity is unclear. [Git credential helpers](https://git-scm.com/docs/gitcredentials)

Let GitHub Actions run the project checks. Review their actual results before calling a release verified. Structural checks and evaluation harness checks are not evidence of halakhic accuracy.

## Publish the phone page

In the repository's **Settings → Pages**, select **GitHub Actions**. Then run **Publish phone site** from the Actions tab. Its deployment reports the public URL and packages the full skill download. This workflow is manual; a push alone does not update the page.

Open the deployed page on your phone and send its link to yourself in WhatsApp. Check the title and preview image before sharing it further. Set the repository's About website to the verified Pages URL. The [phone and WhatsApp guide](PHONE-SHARING.md) explains the sharing behavior and preview metadata; the [verification record](VERIFICATION.md) distinguishes local inspection from the remaining live checks.

## Help people find it

Use a clear README, one installation command, source-linked examples, a license, and an evaluation report that distinguishes measured results from future plans.

Use this public metadata once the repository is ready:

| Field | Ready-to-use text |
| --- | --- |
| Repository | `OWNER/posek` — replace `OWNER` with the chosen user or organization. |
| Public title | Posek — An Orthodox AI Rabbi for Torah and Halacha |
| Subtitle | Moirah D’Asrah |
| GitHub About | An open-source Orthodox AI Rabbi and AI Posek for Torah, halacha, and divrei Torah. Source-based teshuvos, vortlach, and shiur preparation for Claude Code and Codex. |
| Topics | `ai-rabbi`, `ai-posek`, `ai-torah`, `divrei-torah`, `parsha`, `halacha`, `halakhah`, `torah`, `psak`, `jewish-studies`, `agent-skills`, `claude-code`, `codex` |

After creating the repository, use the isolated helper from above to apply the About text and topics. This updates the explicitly named public repository. Verify `PUBLISHER` and `OWNER` before running it:

```sh
test "$(posek_gh api user --jq .login)" = "$PUBLISHER" || {
  printf '%s\n' 'Stop: authenticated account does not match PUBLISHER.' >&2
  exit 1
}

posek_gh repo edit "$OWNER/posek" \
  --description 'An open-source Orthodox AI Rabbi and AI Posek for Torah, halacha, and divrei Torah. Source-based teshuvos, vortlach, and shiur preparation for Claude Code and Codex.' \
  --add-topic ai-rabbi --add-topic ai-posek --add-topic ai-torah \
  --add-topic divrei-torah --add-topic parsha \
  --add-topic halacha --add-topic halakhah --add-topic torah \
  --add-topic psak --add-topic jewish-studies --add-topic agent-skills \
  --add-topic claude-code --add-topic codex
```

The [launch copy](LAUNCH.md) explains the AI Rabbi, AI Posek, and AI Torah learning use cases, the source method, and the current evidence. Keep those terms in useful descriptions of what the project does. Avoid repeating keywords without adding information.

- **GitHub topics:** the topics above describe the project and aid discovery; they do not guarantee traffic or search placement. [Topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- **GitHub skill discovery:** current CLI documentation includes `gh skill search halacha`, which searches public skill names and descriptions. After the isolated setup above, `posek_gh skill publish --tag v0.1.0` validates skills and publishes a release using the selected account. Check `gh skill --help` first: the installed CLI may not support these commands. Publication is an external action; `--dry-run` is validation only. [Search](https://cli.github.com/manual/gh_skill_search), [publish](https://cli.github.com/manual/gh_skill_publish)
- **skills.sh:** its documented route is a public GitHub skill installed through the Skills CLI. Real installations supply the telemetry used for listings and rankings; listing timing and discoverability are not guaranteed. Install counts measure adoption, not correctness. [Listing FAQ](https://skills.sh/docs/faq)
- **Plugin distribution:** OpenAI recommends packaging reusable skills as plugins for its directory. This adds a separate packaging and review path; a public skill repository can launch first. [OpenAI packaging](https://developers.openai.com/plugins/build/plugins)

After replacing `OWNER`, the portable project-scoped installation command is:

```sh
npx skills add OWNER/posek --skill posek --agent claude-code --agent codex
```

The CLI supports these explicit agent and skill selections. Readers should review the source before installation. [Skills CLI](https://github.com/vercel-labs/skills)

Describe the evidence consistently wherever you announce it: the practical halacha suite has 24 development cases, and a separate divrei Torah suite has ten editorial cases; the small AI-reviewed pilot covered nine selected cases, with both Posek and the baseline passing all nine. No improvement over the baseline or expert validation has been established. Link the [recorded results](../benchmarks/RESULTS.md), and update public claims only when new evidence supports them.
