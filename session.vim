let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/arbeider/waterworld
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +7 run.jl
badd +81 env_waterworld.py
badd +137 slett.py
badd +1 environment_interface.py
badd +45 env_mock.py
argglobal
%argdel
$argadd run.jl
$argadd env_waterworld.py
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit run.jl
argglobal
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 7 - ((5 * winheight(0) + 31) / 62)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 7
normal! 0
tabnext
edit env_mock.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 127 + 127) / 255)
exe 'vert 2resize ' . ((&columns * 127 + 127) / 255)
argglobal
if bufexists(fnamemodify("env_mock.py", ":p")) | buffer env_mock.py | else | edit env_mock.py | endif
if &buftype ==# 'terminal'
  silent file env_mock.py
endif
balt env_waterworld.py
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
67
normal! zo
let s:l = 45 - ((44 * winheight(0) + 31) / 62)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 45
normal! 039|
wincmd w
argglobal
if bufexists(fnamemodify("env_waterworld.py", ":p")) | buffer env_waterworld.py | else | edit env_waterworld.py | endif
if &buftype ==# 'terminal'
  silent file env_waterworld.py
endif
balt environment_interface.py
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
106
normal! zo
126
normal! zo
let s:l = 83 - ((16 * winheight(0) + 31) / 62)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 83
normal! 058|
wincmd w
exe 'vert 1resize ' . ((&columns * 127 + 127) / 255)
exe 'vert 2resize ' . ((&columns * 127 + 127) / 255)
tabnext
edit environment_interface.py
argglobal
if bufexists(fnamemodify("environment_interface.py", ":p")) | buffer environment_interface.py | else | edit environment_interface.py | endif
if &buftype ==# 'terminal'
  silent file environment_interface.py
endif
balt env_waterworld.py
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 86 - ((58 * winheight(0) + 31) / 62)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 86
normal! 025|
tabnext 2
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
