# Coq  
# A Docker image for using Coq interactive theorem prover  
#  
FROM ocaml/opam:debian  
  
# coq 8.8.0 req 4.02.3 <= ocaml  
ARG OCAML_VER=4.05.0  
ARG COQ_VER=8.8.0  
ARG OPAMJOBS=2  
ARG OPAMVERBOSE=-v  
  
# package description  
LABEL name="coq" \  
version="3" \  
description="A Docker image for using Coq interactive theorem prover
${COQ_VER}" \  
coq_version="${COQ_VER}" \  
ocaml_version="${OCAML_VER}" \  
author="eldesh <nephits@gmail.com>"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
USER root  
WORKDIR /  
# delete user [opam]; setup user [coq]  
RUN userdel --remove opam \  
&& rm /etc/sudoers.d/opam \  
&& groupadd --gid 1000 coq \  
&& useradd --create-home --shell /usr/bin/bash \  
\--groups sudo --uid 1000 --gid 1000 coq \  
&& echo "coq:coq" | chpasswd \  
&& echo 'coq ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/coq  
  
# switch user from [opam] to [coq]  
USER coq  
WORKDIR /home/coq  
ENV HOME=/home/coq  
  
# ocaml init script  
COPY dot.ocamlinit /home/coq/.ocamlinit  
  
# setup opam ; install coq  
RUN opam init ${OPAMVERBOSE} \--yes \  
&& eval `opam config env` \  
&& sudo chown coq:coq ~/.ocamlinit \  
&& echo '# OPAM configuration' >> ~/.profile \  
&& echo '. ~/.opam/opam-init/init.sh >/dev/null 2>&1 || true' >> ~/.profile \  
&& opam switch ${OCAML_VER} ${OPAMVERBOSE} \  
&& eval `opam config env` \  
&& opam repo add official https://opam.ocaml.org/ \  
&& opam install ${OPAMVERBOSE} \--yes coq.${COQ_VER}  
  
CMD coqc --version  
  

