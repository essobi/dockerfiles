FROM ubuntu:17.04  
MAINTAINER GARCIN David <david.garcin.pro@gmail.com>  
  
ADD configure.sh /configure  
RUN chmod +x /configure  
RUN /configure  
  
ADD start.sh /start  
RUN chmod +x /start  
  
VOLUME ["/home/sshuser"]  
  
EXPOSE 22  
CMD ["/start"]  

