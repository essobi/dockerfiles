# OPAM for debian-stable with local switch of OCaml 4.05.0  
FROM ocaml/ocaml:debian-stable  
LABEL distro_style="apt" distro="debian" distro_long="debian-stable"
arch="x86_64" ocaml_version="4.05.0" opam_version="master"
operatingsystem="linux"  
RUN apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install aspcud && \  
git clone -b master git://github.com/ocaml/opam /tmp/opam && \  
sh -c "cd /tmp/opam && make cold && make cold-install && mkdir -p
/usr/local/share/opam && cp shell/wrap-build.sh /usr/local/share/opam && echo
'wrap-build-commands: \"/usr/local/share/opam/wrap-build.sh\"' >>
/etc/opamrc.userns && cp shell/wrap-install.sh /usr/local/share/opam && echo
'wrap-install-commands: \"/usr/local/share/opam/wrap-install.sh\"' >>
/etc/opamrc.userns && cp shell/wrap-remove.sh /usr/local/share/opam && echo
'wrap-remove-commands: \"/usr/local/share/opam/wrap-remove.sh\"' >>
/etc/opamrc.userns && rm -rf /tmp/opam" && \  
echo 'opam ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/opam && \  
chmod 440 /etc/sudoers.d/opam && \  
chown root:root /etc/sudoers.d/opam && \  
adduser --disabled-password --gecos '' opam && \  
passwd -l opam && \  
chown -R opam:opam /home/opam  
USER opam  
ENV HOME /home/opam  
WORKDIR /home/opam  
RUN mkdir .ssh && \  
chmod 700 .ssh && \  
git config --global user.email "docker@example.com" && \  
git config --global user.name "Docker CI" && \  
sudo -u opam sh -c "git clone -b master git://github.com/ocaml/opam-
repository" && \  
sudo -u opam sh -c "cd /home/opam/opam-repository && opam admin upgrade && git
checkout -b v2 && git add . && git commit -a -m 'opam admin upgrade'" && \  
sudo -u opam sh -c "opam init -a -y --comp ocaml-base-compiler.4.05.0
/home/opam/opam-repository" && \  
sudo -u opam sh -c "opam install -y depext travis-opam"  
ENTRYPOINT [ "opam", "config", "exec", "--" ]  
CMD [ "bash" ]  

