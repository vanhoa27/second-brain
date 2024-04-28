---
tags:
  - linux
---
# Terminal Tricks
- \<C-a>\<C-d> $\rightarrow$ Detach Terminal, but upkeep operation (_keep pdf open_)
- \<C-l> $\rightarrow$ clear Terminal

## How to merge pdfs + outline
```bash
pdftk *.pdf cat output <pdfname>.pdf
```

```bash
pdftk <input>.pdf update_info <outline>.txt output
<output>.pdf
```

```txt
BookmarkBegin
BookmarkTitle: Ein Titel 
BookmarkLevel: 1
BookmarkPageNumber: 1
```