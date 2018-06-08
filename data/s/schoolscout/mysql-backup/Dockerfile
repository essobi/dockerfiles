FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get -y install mysql-client openssh-client gnupg2  
  
RUN mkdir /backup \  
&& mkdir /root/.ssh \  
&& chmod 0700 /root/.ssh  
  
COPY entrypoint.sh /  
CMD /entrypoint.sh  

