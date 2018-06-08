FROM alpine:latest  
  
MAINTAINER Adolfo E. García <adolfo.garcia.cr@gmail.com>  
  
RUN apk update && apk upgrade  
RUN apk add curl bzip2 perl-digest-sha1 gnupg ca-certificates bash sudo git  
  
RUN gpg --keyserver pgp.mit.edu --recv-keys 0x6D7198DE  
  
# See https://blog.tersmitten.nl/how-to-ultimately-trust-a-public-key-non-
interactively.html  
RUN echo "$( \  
gpg --list-keys --fingerprint \  
| grep 6D7198DE -A 1 | tail -1 \  
| tr -d '[:space:]' | awk 'BEGIN { FS = "=" } ; { print $2 }' \  
):6:" | gpg --import-ownertrust;  
  
WORKDIR /tmp  
  
ENV NIXPKGS="/nixpkgs"  
ENV USER=root  
RUN echo 'nixbld:x:998:nobody' >> /etc/group  
  
RUN curl -O https://nixos.org/nix/install  
RUN curl -O https://nixos.org/nix/install.sig  
  
RUN gpg2 --verify ./install.sig && sh ./install  
  
RUN rm install install.sig  
  
RUN echo ". /root/.nix-profile/etc/profile.d/nix.sh" >> /root/.profile  
  
RUN . /root/.nix-profile/etc/profile.d/nix.sh && nix-channel --add
https://nixos.org/channels/nixpkgs-unstable && nix-channel --update && nix-env
-u  
  
VOLUME /nixpkgs  
  
WORKDIR /nixpkgs  
  
CMD sh -l  

