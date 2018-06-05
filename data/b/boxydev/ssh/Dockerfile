FROM debian  
MAINTAINER Matthieu Mota <matthieumota@gmail.com>  
  
ENV USERNAME matthieu  
ENV USERID 1000  
ENV SSHPORT 22  
ENV PASSWORD matthieu  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
openssh-server  
RUN mkdir /var/run/sshd  
RUN mkdir /var/www  
  
WORKDIR /var/www  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
CMD ["/run.sh"]

