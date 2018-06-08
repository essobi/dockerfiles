FROM ocaml/opam  
ENV COQ_VERSION 8.7.2  
RUN git -C opam-repository pull \  
&& opam update \  
&& opam install coq.$COQ_VERSION  

