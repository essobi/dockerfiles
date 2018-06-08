FROM ocaml/opam:alpine-3.5_ocaml-4.04.2  
RUN sudo apk update  
RUN sudo apk --no-cache add openssl ca-certificates nodejs bash vim python  
USER 0  
RUN sudo ln -s /usr/bin/node /usr/bin/nodejs  
WORKDIR /home/opam/reuse-lang  
ENTRYPOINT /home/opam/reuse-lang/dev-env/entrypoint.sh  

