FROM ocaml/opam-dev:alpine  
RUN sudo apk add jq  
RUN cd /home/opam/opam-repository && git checkout master && git pull origin
master && opam admin upgrade && opam update  
RUN opam remote add mir-dev https://github.com/mirage/mirage-dev.git  
COPY . /home/opam/src  
RUN sudo chown -R opam /home/opam/src  
RUN opam remote add mirage /home/opam/src  
RUN opam install -y --dry-run --json pkg.json mirage-core.0  
RUN jq -r '.solution | .[] | .install | "\\(.name).\\(.version)"' pkg.json >
pkg.txt  
RUN cat pkg.txt  
RUN /home/opam/src/scripts/jbuilder-check.sh pkg.txt  
RUN opam depext -yj4 -i `cat no-jbuild.txt`  

