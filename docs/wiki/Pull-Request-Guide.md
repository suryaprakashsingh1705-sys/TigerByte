# 🐯 TigerByte Pull Request Guide

Note: This file is for the `docs/wiki` folder. Do not post it directly to the GitHub Wiki — a maintainer will move it later.

Welcome to the TigerByte PR guide! This page explains what a Pull Request (PR) is, how to use our friendly PR template, and includes an example PR you can use as a model. We keep things playful and practical — like TigerByte itself.

## What is a Pull Request?

A Pull Request (PR) is a request to merge your changes into the main repository. It lets maintainers and contributors review code, discuss design, and ensure the project stays healthy. Think of a PR as a polite roar asking to join the pride.

## Where the template is

The repository contains a PR template at:

`.github/pull_request_template.md`

When you open a new PR on GitHub, this template will automatically populate the description. Fill the sections and replace placeholders before submitting.

## How to use the PR template

1. Create a branch for your change: `git checkout -b feat/some-fun-thing`
2. Make your changes and commit them with clear messages.
3. Push your branch and open a Pull Request on GitHub.
4. The template will appear in the PR description. Fill these fields:
   - Related Issue: Use `Fixes #<number>` if the PR resolves an issue.
   - What This PR Does: Brief summary of the change.
   - Why It Matters: Explain benefits or user-facing improvements.
   - Checklist: Mark items you completed (testing, docs, changelog).
   - Notes for Reviewers: Tell reviewers anything special to look at.

Tips:
- Keep PRs small and focused — easier to review and faster to merge.
- If the change is large, summarize sections and link to detailed design docs.
- Add unit tests or simple manual test steps where practical.

## Example Pull Request (fill-in example)

Related Issue: Fixes #12

### 🧠 What This PR Does
Adds the initial PR template for TigerByte and a short guide in `docs/wiki`.

### 🐾 Why It Matters
Helps contributors submit clean, consistent PRs. Makes reviews faster and friendlier.

### ✅ Checklist
- [x] Code runs locally (basic smoke test)
- [x] Docs updated: added `docs/wiki/Pull-Request-Guide.md`
- [x] I’ve roared in celebration after saving the file 🐅

### 💬 Notes
This was fun to write — TigerByte makes open source feel alive! — `VIDHITTS`

---

## After your PR is opened

- Respond to review comments kindly.
- Keep commits tidy; maintainers may ask to squash or rebase before merging.
- If your PR needs help, ask for it. We're a friendly community.

## Labels to use (suggestions)

- `documentation`
- `good first issue` (for beginner-friendly contributions)
- `hacktoberfest` (for seasonal events)

## Final note

Thanks for contributing — every fix, doc tweak, and example makes TigerByte better. Roar loudly and code boldly! 🐯

---

Contributor: `VIDHITTS`
