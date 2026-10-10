# Skills

[![skills.sh](https://skills.sh/b/lokidotdev/skills)](https://skills.sh/lokidotdev/skills)

A growing collection of agent skills for Claude Code, Codex, Cursor, Amp, Gemini CLI and other agents that support the open [`SKILL.md`](https://agentskills.io) format.

Each skill is a self-contained folder: a `SKILL.md` with instructions, plus optional `references/`, `templates/` and `scripts/` that the agent loads only when it needs them.

## Available skills

| Skill | What it does |
|---|---|
| [ux-first-design](skills/ux-first-design/SKILL.md) | UX-first product design for creating, updating, revamping and auditing interfaces (SaaS dashboards, tables, onboarding, settings, AI features, mobile apps). It starts from the user's job, the flow, every state and its consequences, then applies the visual layer. Includes a contrast checker and a UX lint script. |

More skills are on the way.

## Install

### With the `skills` CLI (any supported agent)

```bash
# all skills in this repo
npx skills add lokidotdev/skills

# a single skill
npx skills add lokidotdev/skills --skill ux-first-design

# list the skills in this repo without installing
npx skills add lokidotdev/skills -l
```

Browse them on [skills.sh](https://skills.sh/lokidotdev/skills).

### Claude Code (manual)

```bash
git clone https://github.com/lokidotdev/skills.git ~/src/skills
mkdir -p ~/.claude/skills
ln -s ~/src/skills/skills/ux-first-design ~/.claude/skills/ux-first-design
```

Use `.claude/skills/` inside a project instead of `~/.claude/skills/` to scope the skill to that project.

### Other agents (manual)

Copy or symlink `skills/<skill-name>/` into the agent's skills directory (for example `~/.agents/skills/`).

## Repository layout

```
skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md              # how to add a new skill
└── skills/
    └── <skill-name>/            # one folder per skill, named exactly like its `name:`
        ├── SKILL.md             # required: frontmatter (name, description) + instructions
        ├── references/          # optional: detail loaded on demand
        ├── templates/           # optional: fill-in templates
        └── scripts/             # optional: helper scripts
```

## License

[MIT](LICENSE)
