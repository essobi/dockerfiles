FROM ocaml/opam:alpine-3.6_ocaml-4.06.0_flambda  
  
USER root  
  
RUN apk --no-cache add vim m4 ncurses  
  
# TODO figure out how to extract only docker/  
RUN VER="17.03.0-ce" && \  
curl -s -L \  
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz | tar -xz -C /tmp \  
&& mv /tmp/docker/* /usr/local/bin && rm -rf /tmp/*  
  
USER opam  
  
RUN cd opam-repository && git pull origin master >/dev/null && cd ..  
  
RUN opam update && opam install -y ocamlfind odoc ounit sexplib cmdliner logs
fmt jbuilder mparser  
  

