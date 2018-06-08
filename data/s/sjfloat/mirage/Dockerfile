  
from sjfloat/ocaml  
  
env DEBIAN_FRONTEND noninteractive  
  
user root  
  
run apt-get update && apt-get install -y \  
libssl-dev \  
pkg-config  
  
user $USER  
run opam switch 4.01.0  
run opam install mirage -y -v  
  
add README.adoc $HOME/README.adoc  

