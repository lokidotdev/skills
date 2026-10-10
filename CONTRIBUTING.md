# Adding a skill

1. **Create a folder** at `skills/<skill-name>/`, for example `skills/my-skill/`. Use lowercase letters, digits and hyphens only, under 64 characters. Don't nest it any deeper.
2. **Add `SKILL.md`** with frontmatter:

   ```markdown
   ---
   name: my-skill            # must match the folder name
   description: "What it does. Use when <trigger phrases and contexts>. Keywords: a, few, searchable, terms."   # max 1024 chars; quote it if it contains ': '
   ---

   # My Skill
   ...instructions...
   ```

3. **Keep `SKILL.md` focused** (under about 300 lines). Move detail into `references/*.md` and say in `SKILL.md` when to read each file. Put reusable fill-ins in `templates/` and deterministic helpers in `scripts/`.
4. **Keep the skill self-contained.** Links between files are relative to the skill folder, with no absolute paths to your machine.
5. **Keep scripts boring.** skills.sh runs security audits: standard library only, no network calls, no shell-outs, no obfuscated or encoded code, nothing that writes outside the paths the user passes in.
6. **Don't commit third-party or private source material.** Research inputs such as screenshots go in `_local/`, which git ignores.
7. **Test it**: check that the frontmatter parses, run any scripts, run `npx skills add lokidotdev/skills -l` to confirm it's detected, and try a few real prompts that should and shouldn't trigger the skill.
8. **Add a row** to the "Available skills" table in `README.md`.
