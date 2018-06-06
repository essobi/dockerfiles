FROM ocaml/opam:alpine-3.4_ocaml-4.04.2  
LABEL distro_style="apk" distro="alpine" distro_long="alpine-3.4"
arch="x86_64" ocaml_version="4.04.2" opam_version="1.2"
operatingsystem="linux"  
  
RUN sudo apk update && sudo apk add \  
alpine-sdk bash ncurses-dev m4 perl gmp-dev zlib-dev libsodium-dev libffi-dev  
  
RUN opam repository add git https://github.com/ocaml/opam-repository.git &&
opam update  
  
WORKDIR builder/  
ADD . .  
  
RUN opam switch import export-service.install  

