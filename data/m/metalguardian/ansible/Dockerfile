FROM ubuntu:latest  
MAINTAINER Ivan Pushkin <imetalguardi+docker@gmail.com>  
  
ENV TERM xterm  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv
6125E2A8C77F2818FB7BD15B93C4A3FD7BB9C367  
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu $(cat /etc/lsb-
release | grep DISTRIB_CODENAME | cut -d= -f2) main\n \  
deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu $(cat /etc/lsb-release
| grep DISTRIB_CODENAME | cut -d= -f2) main" \  
> /etc/apt/sources.list.d/ansible.list  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install
\  
ansible \  
ssh \  
nano  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts  
  
RUN mkdir /ansible  
  
# add user "docker" to use it as default user for working with files  
RUN yes "" | adduser --uid=1000 --disabled-password docker  
RUN echo "docker ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
USER docker  
  
WORKDIR /ansible  
  
CMD ["/bin/true"]  

