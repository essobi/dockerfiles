FROM ocaml/opam:alpine-3.6_ocaml-4.06.0_flambda  
  
USER root  
  
RUN apk --no-cache add vim m4 ncurses  
  
COPY \--from=docker:17.12 /usr/local/bin/docker /usr/local/bin/docker  
  
ADD https://github.com/ocaml/opam-repository/archive/master.tar.gz
/tmp/repo.tgz  
  
RUN tar -xzf /tmp/repo.tgz -C opam-repository --strip=1 && chown -R opam opam-
repository  
  
USER opam  
  
RUN opam update && opam upgrade -y && \  
opam install -y odoc ounit sexplib cmdliner logs fmt mparser  
  

