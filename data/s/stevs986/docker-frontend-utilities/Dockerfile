FROM node:6.9.1  
MAINTAINER Sladjan Nikolic <sladjan.nikolic986@gmail.com>  
  
# Install Bower & Grunt  
ADD ./front.sh /home/front.sh  
CMD chmod +x /home/front.sh  
ADD ./entry.sh /home/entry.sh  
CMD chmod +x /home/entry.sh  
RUN /home/entry.sh  
RUN usermod -u 111 node  
USER r  
RUN whoami  
RUN /home/front.sh  
  
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

