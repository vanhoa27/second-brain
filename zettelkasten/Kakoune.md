---
id: Kakoune
aliases:
  - Creating aliases and defining aliases
tags:
  - editors
---

# Creating aliases and defining aliases
- alias global tag ctags-search
-`define-command tagR %{ nop %sh{ ctags -R --exclude=build --exclude=test --exclude=.git $(dirname)} }`

## Hooks for filetypes 
```
def filetype-hook -params 2 %{ hook global WinSetOption "filetype=(%arg{1})" %arg{2} }
filetype-hook c|cpp %{
	set-option buffer formatcmd 'astyle'
}
hook global BufSetOption filetype=python %{
    set-option buffer formatcmd 'black'
}
```
