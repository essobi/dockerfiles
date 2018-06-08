  
from sjfloat/ocaml  
  
env DEBIAN_FRONTEND noninteractive  
  
user root  
  
run opam install ounit  
  
workdir /tmp  
run wget https://github.com/exercism/cli/releases/download/v2.2.1/exercism-
linux-64bit.tgz  
run tar xvf exercism-linux-64bit.tgz  
run chmod +x exercism  
run mv exercism /usr/local/bin/  
run rm -rf /tmp/*  
  
workdir $HOME  
user $USER  
add README.adoc $HOME/  

