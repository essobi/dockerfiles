FROM alpine:latest  
MAINTAINER Jurrian Fahner  
  
#Install packages  
RUN apk update && apk upgrade && apk add bash openssh git  
  
#Copy scripts  
ADD addkey /usr/bin/  
ADD key /usr/bin/  
ADD recreatehostfiles /usr/bin/  
ADD repo /usr/bin/  
  
#Harden ssh server  
ADD sshd_config /etc/ssh/  
  
#Empty motd  
RUN echo -n "" > /etc/motd  
  
#Create initial host keys  
WORKDIR /etc/ssh  
RUN ssh-keygen -N "" -t ed25519 -f ssh_host_ed25519_key < /dev/null  
#RUN ssh-keygen -N "" -t rsa -b 4096 -f ssh_host_rsa_key < /dev/null  
#Create git user  
RUN adduser -D -s /usr/bin/git-shell git  
RUN passwd -d -u git  
  
#Create location where the repositories should be stored  
#See for more information: https://git-scm.com/book/en/v1/Git-on-the-Server-
Setting-Up-the-Server  
RUN mkdir -p /opt/git  
WORKDIR /opt  
RUN chown -R git: ./git  
  
#Configure ssh  
USER git  
WORKDIR /home/git  
RUN mkdir .ssh  
RUN chmod 700 .ssh  
RUN touch .ssh/authorized_keys  
RUN touch .ssh/known_hosts  
RUN chmod 600 .ssh/authorized_keys  
  
#Usual docker stuf...  
EXPOSE 22  
USER root  
CMD /usr/sbin/sshd -D  

