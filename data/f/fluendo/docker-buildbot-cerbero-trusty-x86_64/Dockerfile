FROM fluendo/docker-buildbot-trusty-x86_64  
  
MAINTAINER fluendo  
  
# Install required packages  
RUN easy_install requests tinys3  
  
# To avoid any interactive question  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get -y install sudo wget libnss-ldap  
RUN chmod 777 /worker  
  
COPY run.sh .  
CMD ["./run.sh"]  

