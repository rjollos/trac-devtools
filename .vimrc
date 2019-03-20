syntax on
filetype indent plugin on

"Show line numbers
set number
"Highlight search matches
set hls

set list
set listchars=eol:¬,tab:▸-
set backspace=indent,eol,start

highlight BadWhitespace ctermbg=red guibg=darkred

"Strip trailing whitespace
"http://vim.wikia.com/wiki/Remove_unwanted_spaces#Automatically_removing_all_trailing_whitespace
autocmd FileType html,javascript,python,css,matlab,rst
    \ autocmd BufWritePre <buffer> :%s/\s\+$//e

"Python indentation and whitespace
au FileType python,matlab
    \ setlocal tabstop=4 softtabstop=4 shiftwidth=4 textwidth=79
    \ expandtab autoindent fileformat=unix
    \| match BadWhitespace /\s\+$/

"Frontend indentation
au FileType javascript,html,css 
    \ setlocal tabstop=2 softtabstop=2 shiftwidth=2

au FileType yaml setlocal ts=2 sts=2 sw=2 expandtab 

"Expand %% to active directory
cnoremap <expr> %%  getcmdtype() == ':' ? expand('%:h').'/' : '%%'

"Add shortcut for saving a file that requires elevated permissions
cnoremap w!! execute 'silent! write !sudo tee % >/dev/null' <bar> edit!

