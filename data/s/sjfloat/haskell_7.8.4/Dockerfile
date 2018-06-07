  
from sjfloat/dev  
  
env DEBIAN_FRONTEND noninteractive  
  
user root  
  
#  
# get stack  
#  
run wget -q -O-
https://s3.amazonaws.com/download.fpcomplete.com/debian/fpco.key | apt-key add
-  
run echo 'deb http://download.fpcomplete.com/debian/jessie stable main'| tee
/etc/apt/sources.list.d/fpco.list  
run apt-get update && apt-get install -y \  
stack \  
libtinfo-dev  
run apt-get clean  
run rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
env HOME /home/$USER  
add stack.yaml $HOME/.stack/global/stack.yaml  
run chown -R ${USER}: $HOME  
  
user $USER  
workdir $HOME  
run stack setup  
run stack install cabal-install  
run stack path --bin-path | path-to-setup stack  
  
run . $HOME/.profile && cabal update && cabal install \  
ghc-mod \  
happy \  
hdevtools \  
hlint \  
hoogle \  
HUnit \  
parsec \  
test-framework \  
test-framework-hunit  
  
run echo "set path = (\$path $HOME/.cabal/bin)" > $HOME/.cshrc.d/z_cabal.csh  
run echo "export PATH=\$PATH:$HOME/.cabal/bin" > $HOME/.profile.d/z_cabal.sh  
add haskeline $HOME/.haskeline  
add hdevtools.vim $HOME/.vim/plugin/  
add ghc-mod.vim $HOME/.vim/plugin/  
  
#  
# see docker bugs #6119 and #9934  
# hack, for some reason, ownership is changing too root on second .vim/plugin
add  
#  
user root  
run chown -R ${USER}: \  
$HOME/.vim/plugin \  
$HOME/.haskeline  
  
user $USER  
# ghcmod.vim  
# ghcmod.vim requires vimproc  
run git clone https://github.com/Shougo/vimproc.vim.git
$HOME/.vim/bundle/vimproc.vim  
workdir $HOME/.vim/bundle/vimproc.vim  
run make  
  
workdir $HOME/.vim/bundle/  
run wget -O /tmp/ghcmod.vim.zip
"http://www.vim.org/scripts/download_script.php?src_id=23482" \  
&& unzip /tmp/ghcmod.vim.zip  
workdir $HOME  
  
cmd $SHELL -l  
  
# vim:ft=dockerfile  

