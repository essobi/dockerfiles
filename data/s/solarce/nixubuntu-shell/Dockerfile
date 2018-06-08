FROM ubuntu:trusty  
# A dockerfile to setup an ubuntu container to use with your  
# existing home dir but isolated for package installs  
MAINTAINER Brandon Burton <brandon@inatree.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN adduser --shell /bin/bash --gecos "User" -ingroup users --disabled-
password --home /home/ubuntu ubuntu  
RUN apt-get --quiet --yes install sudo vim rsync ssh zsh curl build-essential
git \  
libcurl3-gnutls libdbd-sqlite3-perl libdbi-perl libwww-curl-perl xz-utils  
RUN echo "%users ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/users  
WORKDIR /home/ubuntu  
USER ubuntu  
ENV USER=ubuntu  
ENV SHELL=/bin/bash  
RUN curl https://nixos.org/nix/install | sh  
RUN echo ". /home/ubuntu/.nix-profile/etc/profile.d/nix.sh" >>
/home/ubuntu/.bashrc  
RUN ["/bin/bash", "-c", "source /home/ubuntu/.nix-profile/etc/profile.d/nix.sh
&& nix-env -i nix-repl nixops nixbang"]  
  
ENTRYPOINT /bin/bash  

