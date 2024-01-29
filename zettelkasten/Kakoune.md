---
id: Kakoune
aliases:
  - Creating aliases and defining aliases
tags:
  - editors
---
## Getting started with [Kakoune](http://kakoune.org/)
### Philosophy
- Kakoune is inspired by Vim but it tries to adhere more to the Unix philosphy
	- `Do one thing and do it well`
- it doesn't try to reinvent the **wheel**, but integrate existing shell commands
- Kakoune's keybindings are more "consitent"
- The **keybindings** differ from vim in the following:
	- Motion before the *action* 
	- *e.g.* first a word is highlighted with *w* and then deleted with *d*
	- there is no *visual mode*
### Basic setting
```bash
# Set Theme
colorscheme gruvbox 

# Line numbers
add-highlighter global/ number-lines -hlcursor -relative

# Show matching brackets
add-highlighter global/ show-matching 

# Indent width
set-option global tabstop 4
set-option global indentwidth 4
set-option global scrolloff 2,3

# Change the default command
set-option global grepcmd 'grep -RHn --exclude-dir=build --exclude=*.git* --exclude=tags --exclude-dir=node_modules'
```
- the context `global` is specified after the command
### Creating mappings
```bash
map global user p '!xclip -o<ret>'
map global user y '<a-|>xclip -i -selection clipboard<ret>'
map global normal <space> , -docstring 'User mode'
map global user ] <a-i>w':tag<ret>' -docstring 'Tags'
map global user / ':comment-line<ret>' -docstring 'Comment'
map global normal <c-v> ':comment-line<ret>'
map global user g ':grep ''''<left>' -docstring 'grep'
map global user G ':grep -i ''''<left>' -docstring 'grep'
```
### Advanced settings
- Creating aliases and defining aliases
```bash
alias global tag ctags-search
alias global fmt format-buffer
define-command tagR %{ nop %sh{ ctags -R --exclude=build --exclude=test --exclude=.git $(dirname)} }
```
- Hooks for filetypes 
```bash
# defining a shorthand
def filetype-hook -params 2 %{ hook global WinSetOption "filetype=(%arg{1})" %arg{2} }

# Setting Formatters
filetype-hook c|cpp %{
	set-option buffer formatcmd 'astyle'
}
hook global BufSetOption filetype=python %{
    set-option buffer formatcmd 'black'
}
```