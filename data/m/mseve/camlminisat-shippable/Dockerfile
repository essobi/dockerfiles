FROM ubuntu:16.04  
  
MAINTAINER Michele Sevegnani <michele.sevegnani@glasgow.ac.uk>  
  
# Install debs  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install
sudo \  
git-core \  
pkg-config \  
build-essential \  
m4 \  
ocaml \  
ocaml-native-compilers \  
aspcud \  
opam \  
git-core \  
zlib1g-dev \  
minisat && \  
DEBIAN_FRONTEND=noninteractive apt-get clean && \  
echo 'minisat ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/minisat && \  
chmod 440 /etc/sudoers.d/minisat && \  
chown root:root /etc/sudoers.d/minisat && \  
adduser --disabled-password --gecos '' minisat && \  
passwd -l minisat && \  
chown -R minisat:minisat /home/minisat  
  
USER minisat  
ENV HOME /home/minisat  
ENV OPAMJOBS 4  
WORKDIR /home/minisat  
  
# Configure OPAM  
RUN sudo -u minisat sh -c "opam init -a -y" && \  
sudo -u minisat sh -c "opam switch -y 4.03.0" && \  
sudo -u minisat sh -c "opam install -y ocamlfind"  
  
ENTRYPOINT [ "opam", "config", "exec", "--" ]  
CMD [ "sh" ]  

