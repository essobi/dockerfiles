FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get -y install openssh-server  
RUN apt-get -y install wget  
RUN apt-get -y install unzip  
RUN apt-get -y install vim-tiny  
RUN apt-get -y install curl  
  
RUN apt-get clean  
  
ADD onstart.sh /  
RUN chmod +x /onstart.sh  
ENV MAILGUN_API ""  
ENV MAILGUN_DOMAIN ""  
ENV MAILGUN_TO ""  
RUN useradd -m admin  
EXPOSE 22  
ENV ADMINPASS adminpass  
ENV ROOTPASS rootpass  
RUN mkdir /var/run/sshd  
CMD ["echo admin:$ADMINPASS | chpasswd && echo root:$ROOTPASS | chpasswd &&
/onstart.sh && /usr/sbin/sshd -D"]  
ENTRYPOINT ["/bin/sh","-c"]  
  

