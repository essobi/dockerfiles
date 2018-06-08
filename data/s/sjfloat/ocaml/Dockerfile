  
from sjfloat/dev  
  
maintainer steve@jonescape.com  
  
env DEBIAN_FRONTEND noninteractive  
  
user root  
  
run apt-get update && apt-get install -y \  
m4 \  
ocaml-base \  
ocaml-nox \  
rlwrap \  
vim-nox \  
unzip  
  
run apt-get clean  
run rm -rf /var/lib/apt/lists/*  
  
env HOME /home/$USER  
workdir $HOME  
add https://raw.github.com/ocaml/opam/master/shell/opam_installer.sh
$HOME/opam_installer.sh  
run /bin/sh $HOME/opam_installer.sh /usr/bin > opam_installer.out 2>&1  
  
user $USER  
run opam init -v -y > opam-init.out 2>&1  
run opam switch 4.04.0  
  
run eval `opam config env` && opam install -y \  
camlp4 \  
core \  
batteries \  
merlin \  
oasis \  
utop  
  
add vim.patch /tmp/vim.patch  
add ocamlinit $HOME/.ocamlinit  
run patch ~/.vimrc /tmp/vim.patch  
run ln -s $HOME/.opam/opam-init/init.csh $HOME/.cshrc.d/  
run ln -s $HOME/.opam/opam-init/init.sh $HOME/.profile.d/  
  
user root  
run rm -rf /tmp/* /var/tmp/*  
  
user $USER  
cmd $SHELL -l  

