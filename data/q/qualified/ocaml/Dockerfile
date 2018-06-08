FROM buildpack-deps:xenial  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
ENV OPAMROOT=/opt/opam \  
OPAMCOLOR=never  
  
# Use system OCaml from ocaml-nox (4.02.3-5ubuntu2)  
# If we need to rebuild this image and the version is off,  
# we can try `opam switch 4.02.3`.  
RUN set -ex; \  
mkdir -p $OPAMROOT; \  
chown codewarrior:codewarrior $OPAMROOT; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
ocaml-nox \  
opam \  
camlp4 \  
rsync \  
aspcud \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
RUN set -ex; \  
opam init; \  
opam update -y; \  
opam install -y \  
ounit.2.0.6 \  
batteries.2.5.3 \  
core.113.33.03 \  
;  
  
# opam config env  
ENV CAML_LD_LIBRARY_PATH=/opt/opam/system/lib/stublibs:/usr/lib/ocaml/stublibs
\  
PERL5LIB=/opt/opam/system/lib/perl5 \  
OCAML_TOPLEVEL_PATH=/opt/opam/system/lib/toplevel \  
PATH=/opt/opam/system/bin:/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
COPY rootfs/workspace /workspace  
  
# To avoid issues related to non-system installations of `ocamlfind`  
RUN echo 'let () = try Topdirs.dir_directory (Sys.getenv
"OCAML_TOPLEVEL_PATH") with Not_found -> ();;' >> $HOME/.ocamlinit  

