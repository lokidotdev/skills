# Adding a skill

1. **Create a folder** at the repo root named in kebab-case, for example `my-skill/`.
2. **Add `SKILL.md`** with frontmatter:

   ```markdown
   ---
   name: my-skill            # must match the folder name
   description: What it does and exactly when an agent should use it (trigger phrases, contexts). Max 1024 characters.
   ---

   # My Skill
   ...instructions...
   ```

3. **Keep `SKILL.md` focused** (ideally under 500 lines). Move detail into `references/*.md` and say in `SKILL.md` when to read each file. Put reusable fill-ins in `templates/` and deterministic helpers in `scripts/`.
4. **Keep the skill self-contained.** Links between files are relative to the skill folder, with no absolute paths to your machine.
5. **Don't commit third-party or private source material.** Research inputs such as screenshots go in `_local/`, which git ignores.
6. **Test it**: check that the frontmatter parses, run any scripts, and try a few real prompts that should and shouldn't trigger the skill.
7. **Add a row** to the "Available skills" table in `README.md`.
