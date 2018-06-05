FROM ubuntu:trusty  
  
MAINTAINER Shorn Tolley "dockerhub-shorn@snkmail.com"  
RUN apt-get update  
RUN apt-get install -y curl dnsutils git  
RUN apt-get install -y openssh-server  
RUN apt-get install -y polipo  
  
# scripts  
ADD run_bastion_tunnels.sh run_bastion_tunnels.sh  
RUN chmod +x run_*.sh  
  
ENV SOCKS_PROXY_PORT=8000  
ENV HTTP_PROXY_PORT=8080  
# you must volume mount the directory this file exists in  
# note: ssh will whine if the file doesn't have very restrictive permissions  
# needs to be something like rw permissions only for owner or something -
that's  
# why you can't mount the files directly from windows (well, AFAIK anyway)  
ENV BASTION_KEYFILE=  
ENV BASTION_USER=  
ENV BASTION_HOST=  
  
EXPOSE $SOCKS_PROXY_PORT  
EXPOSE $HTTP_PROXY_PORT  
  
CMD ["/run_bastion_tunnels.sh"]  
  

