FROM ubuntu:latest  
MAINTAINER David <david@cninone.com>  
  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y openssh-server software-properties-
common python-software-properties \  
supervisor curl nano vim emacs \  
build-essential m4 curl git  
  
RUN add-apt-repository -y ppa:avsm/ppa  
RUN apt-get update && apt-get install -y ocaml ocaml-native-compilers
camlp4-extra opam  
RUN opam init -a && opam remote && echo "eval `opam config env`" >> ~/.bashrc  
RUN opam install -y core mirage utop && eval `opam config env` && mirage
--version  
  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
RUN echo 'root:freego' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  

