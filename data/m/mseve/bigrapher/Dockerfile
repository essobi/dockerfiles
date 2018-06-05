FROM ocaml/ocaml:ubuntu  
  
MAINTAINER Michele Sevegnani <michele.sevegnani@glasgow.ac.uk>  
  
# Install debs and create big user  
RUN apt-get -qy update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install \  
emacs \  
man-db \  
opam \  
graphviz \  
zlib1g-dev \  
minisat && \  
apt-get clean && \  
echo 'big ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/big && \  
chmod 440 /etc/sudoers.d/big && \  
chown root:root /etc/sudoers.d/big && \  
adduser --disabled-password --gecos '' big && \  
passwd -l big && \  
chown -R big:big /home/big  
  
# Configure environment  
ADD bigrapher.el /home/big/.emacs.d/  
ADD HOWTO.md /home/big/  
ADD new_syntax/examples.tar.gz /home/big  
ADD .profile /home/big/  
RUN chown -R big:big /home/big  
  
USER big  
ENV HOME /home/big  
ENV OPAMBUILDDOC 1  
ENV OPAMJOBS 4  
WORKDIR /home/big  
  
# Configure OPAM  
RUN sudo -u big sh -c "opam init -a -y" && \  
sudo -u big sh -c "opam switch -y 4.06.1+flambda" && \  
sudo -u big sh -c "opam repository add glasgow
http://www.dcs.gla.ac.uk/~michele/dcs-opam-repository/" && \  
sudo -u big sh -c "opam install -y bigrapher"  
  
ENTRYPOINT [ "opam", "config", "exec", "--" ]  
CMD [ "bash", "-l" ]

