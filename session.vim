let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/arbeider/progging/waterworld
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 environment_inferface.py
badd +1 manual_control.py
badd +1 serialize.py
badd +1 test_serial.py
badd +37 test_serial.jl
badd +3 interface_testing/test_serial.jl
badd +1 interface_testing/test_serial.py
badd +72 intelligence_samsara_waterworld.py
badd +33 situation_monitor.jl
badd +1 ~/arbeider/peerlearning/perleik/environment_interface.py
badd +19 ~/arbeider/peerlearning/perleik/action_space.py
badd +1 agent_mock.jl
badd +0 ~/arbeider/julia/Hugin.jl/src/Hugin.jl
argglobal
%argdel
$argadd environment_inferface.py
$argadd manual_control.py
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit ~/arbeider/julia/Hugin.jl/src/Hugin.jl
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
exe 'vert 1resize ' . ((&columns * 182 + 182) / 364)
exe 'vert 2resize ' . ((&columns * 181 + 182) / 364)
argglobal
2argu
if bufexists(fnamemodify("~/arbeider/julia/Hugin.jl/src/Hugin.jl", ":p")) | buffer ~/arbeider/julia/Hugin.jl/src/Hugin.jl | else | edit ~/arbeider/julia/Hugin.jl/src/Hugin.jl | endif
if &buftype ==# 'terminal'
  silent file ~/arbeider/julia/Hugin.jl/src/Hugin.jl
endif
balt manual_control.py
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 23 - ((22 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 23
normal! 0
wincmd w
argglobal
2argu
balt ~/arbeider/julia/Hugin.jl/src/Hugin.jl
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 130 - ((129 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 130
normal! 04|
wincmd w
exe 'vert 1resize ' . ((&columns * 182 + 182) / 364)
exe 'vert 2resize ' . ((&columns * 181 + 182) / 364)
tabnext
edit ~/arbeider/peerlearning/perleik/environment_interface.py
argglobal
1argu
if bufexists(fnamemodify("~/arbeider/peerlearning/perleik/environment_interface.py", ":p")) | buffer ~/arbeider/peerlearning/perleik/environment_interface.py | else | edit ~/arbeider/peerlearning/perleik/environment_interface.py | endif
if &buftype ==# 'terminal'
  silent file ~/arbeider/peerlearning/perleik/environment_interface.py
endif
balt manual_control.py
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 72 - ((49 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 72
normal! 0
tabnext 1
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
