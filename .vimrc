" turn on syntax highlighting
syntax on

" detect filetype and adjust indentation according to plugins
filetype plugin indent on

" show line numbers in left column
set number

" show row,column in last line or screen or status line
set ruler

" pressing <TAB> inserts spaces instead of \t
set expandtab

" a <TAB> is equal to 4 spaces
set tabstop=4

" for a file with no filetype-specific indentation rules, keep same level
" of indentation
"set autoindent

" use case insenstive search, except when using capital letters
set ignorecase
set smartcase

" map Shift-H/L to moving between tabs
nnoremap <S-h> gT
nnoremap <S-l> gt

" configure indent based folding
set foldcolumn=1
set foldlevel=4
set foldmethod=indent
set shiftwidth=4
