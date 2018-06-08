FROM ocaml/opam:ubuntu-16.04_ocaml-4.04.2  
MAINTAINER Richard Mortier <mort@cantab.net>  
  
# we need to futz with USERs so let's save on sudos  
USER root  
  
ENV OPAMJOBS=2 OPAMYES=1  
# create the travis user with correct uid/gid to match travis-ci.org  
ENV _UID=2000 _GID=2000  
RUN groupadd --gid $_GID travis \  
&& echo 'travis ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/travis \  
&& chmod 440 /etc/sudoers.d/travis \  
&& chown root:root /etc/sudoers.d/travis \  
&& useradd --no-log-init --shell /bin/bash --home-dir /home/travis -m \  
\--gid travis --uid $_UID travis \  
&& chown -R travis:travis ~travis  
  
# create a working OPAM environment with 4.04.2  
USER travis  
ENV HOME /home/travis  
WORKDIR /home/travis  
  
RUN git clone \--depth 1 -b master git://github.com/ocaml/opam-repository \  
&& opam init -a -y --comp 4.04.2 ~/opam-repository \  
&& opam install -y depext travis-opam \  
# ...and now install mirage  
&& opam depext -u mirage mirage-xen mirage-unix \  
&& opam install mirage mirage-xen mirage-unix  
  
WORKDIR /cwd  
ENTRYPOINT [ "opam", "config", "exec", "--" ]  
CMD [ "mirage" ]  

