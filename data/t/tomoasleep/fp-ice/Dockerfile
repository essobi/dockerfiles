FROM ocaml/opam:alpine_ocaml-4.03.0  
MAINTAINER Tomoya Chiba (@tomoasleep)  
  
WORKDIR /fp-ice  
  
RUN opam switch 4.03.0  
  
ADD opam /fp-ice/  
ADD opam-repository /fp-ice/opam-repository  
  
RUN opam repository add fp-ice-dependencies /fp-ice/opam-repository && \  
opam pin add --no-action fp-ice /fp-ice && \  
opam depext fp-ice  
  
RUN opam install --deps-only fp-ice  
RUN sudo cp $(opam config var lib)/libz3.so /usr/local/lib  
  
ADD . /fp-ice  
RUN sudo chown opam -R /fp-ice  
  
RUN opam install fp-ice  
ENTRYPOINT ["/home/opam/.opam/4.03.0/bin/fp-ice"]  

