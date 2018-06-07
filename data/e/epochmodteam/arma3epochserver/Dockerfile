FROM ubuntu:latest  
  
MAINTAINER Aaron Clark <http://epochmod.com/>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update &&\  
apt-get install -y wget lib32gcc1 lib32stdc++6 redis-server binutils  
  
ADD init.sh /usr/local/bin/init.sh  
RUN chmod +x /usr/local/bin/init.sh  
CMD ["/usr/local/bin/init.sh"]  

