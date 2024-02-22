let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/arbeider/progging/waterworld.py
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
badd +108 manual_control.py
badd +1 serialize.py
badd +1 test_serial.py
badd +29 test_serial.jl
badd +3 interface_testing/test_serial.jl
badd +1 interface_testing/test_serial.py
badd +72 intelligence_samsara_waterworld.py
badd +13 ~/arbeider/progging/waterworld.py/situation_monitor.jl
badd +0 ~/arbeider/peerlearning/perleik/environment_interface.py
badd +19 ~/arbeider/peerlearning/perleik/action_space.py
argglobal
%argdel
$argadd environment_inferface.py
$argadd manual_control.py
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit environment_inferface.py
argglobal
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
tabnext
edit manual_control.py
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
exe 'vert 1resize ' . ((&columns * 181 + 181) / 362)
exe 'vert 2resize ' . ((&columns * 180 + 181) / 362)
argglobal
2argu
balt environment_inferface.py
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
31
normal! zo
70
normal! zo
80
normal! zo
96
normal! zo
102
normal! zo
80
normal! zo
96
normal! zo
102
normal! zo
let s:l = 130 - ((40 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 130
normal! 023|
wincmd w
argglobal
2argu
if bufexists(fnamemodify("~/arbeider/progging/waterworld.py/situation_monitor.jl", ":p")) | buffer ~/arbeider/progging/waterworld.py/situation_monitor.jl | else | edit ~/arbeider/progging/waterworld.py/situation_monitor.jl | endif
if &buftype ==# 'terminal'
  silent file ~/arbeider/progging/waterworld.py/situation_monitor.jl
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
let s:l = 1 - ((0 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 181 + 181) / 362)
exe 'vert 2resize ' . ((&columns * 180 + 181) / 362)
tabnext
edit test_serial.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
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
exe 'vert 1resize ' . ((&columns * 94 + 181) / 362)
exe '2resize ' . ((&lines * 38 + 40) / 80)
exe 'vert 2resize ' . ((&columns * 267 + 181) / 362)
exe '3resize ' . ((&lines * 38 + 40) / 80)
exe 'vert 3resize ' . ((&columns * 267 + 181) / 362)
argglobal
1argu
if bufexists(fnamemodify("test_serial.py", ":p")) | buffer test_serial.py | else | edit test_serial.py | endif
if &buftype ==# 'terminal'
  silent file test_serial.py
endif
balt interface_testing/test_serial.py
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 38) / 77)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 011|
wincmd w
argglobal
1argu
if bufexists(fnamemodify("~/arbeider/progging/waterworld.py/situation_monitor.jl", ":p")) | buffer ~/arbeider/progging/waterworld.py/situation_monitor.jl | else | edit ~/arbeider/progging/waterworld.py/situation_monitor.jl | endif
if &buftype ==# 'terminal'
  silent file ~/arbeider/progging/waterworld.py/situation_monitor.jl
endif
balt test_serial.jl
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 13 - ((12 * winheight(0) + 19) / 38)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 037|
wincmd w
argglobal
1argu
if bufexists(fnamemodify("test_serial.jl", ":p")) | buffer test_serial.jl | else | edit test_serial.jl | endif
if &buftype ==# 'terminal'
  silent file test_serial.jl
endif
balt interface_testing/test_serial.jl
setlocal fdm=marker
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=10
setlocal fen
let s:l = 37 - ((18 * winheight(0) + 19) / 38)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 37
normal! 022|
wincmd w
exe 'vert 1resize ' . ((&columns * 94 + 181) / 362)
exe '2resize ' . ((&lines * 38 + 40) / 80)
exe 'vert 2resize ' . ((&columns * 267 + 181) / 362)
exe '3resize ' . ((&lines * 38 + 40) / 80)
exe 'vert 3resize ' . ((&columns * 267 + 181) / 362)
tabnext
edit ~/arbeider/peerlearning/perleik/environment_interface.py
argglobal
2argu
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
