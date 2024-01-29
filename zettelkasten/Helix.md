---
id: Helix
aliases:
  - Helix
tags:
  - editors
---
## What is [Helix](https://helix-editor.com/)
- Helix is a popluar text editor that is written in [Rust](https://www.rust-lang.org/)
- it is based on kakoune and vim, *but*:
	- it tries to be more *preconfigured*
	- *it just works*
### How to config Helix
- Helix uses a *.toml* file for configuring
- This is how a basic config can look like:
```toml
theme = "onedark"

[editor]
line-number = "relative"
auto-save = true
auto-format = false
color-modes = true
mouse = true
shell = ["zsh", "-c"]
scrolloff = 2

[editor.cursor-shape]
insert = "block"
normal = "block"
# select = "underline"

[editor.file-picker]
hidden = false

[editor.lsp]
auto-signature-help = true
display-signature-help-docs = false

# Remaps
[keys.normal]
"{" = "goto_prev_paragraph"
"}" = "goto_next_paragraph"

[keys.select]
"{" = "goto_prev_paragraph"
"}" = "goto_next_paragraph"
```
### How to fix no syntax highlighting issue
- use: `hx --checkhealth` 
- try building and fetching grammars
```bash
hx -g fetch
hx -g build
```