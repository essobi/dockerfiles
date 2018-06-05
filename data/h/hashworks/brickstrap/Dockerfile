FROM debian:stretch  
MAINTAINER "Justin Kromlinger" <justin.kromlinger@stud.htwk-leipzig.de>  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update  
RUN apt-get -y install libguestfs-tools qemu-user-static gnupg apt-transport-
https dirmngr linux-image-4.9.0-3-amd64  
RUN echo 'deb https://apt.dockerproject.org/repo debian-stretch main' >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo 'deb http://archive.ev3dev.org/ubuntu xenial main' >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 2B210565  
RUN apt-get update  
RUN apt-get -y install brickstrap  
  
CMD ["brickstrap"]  

