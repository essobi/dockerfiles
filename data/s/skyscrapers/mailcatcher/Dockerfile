FROM debian:wheezy  
MAINTAINER skyscrapers "support@skyscrapers.eu"  
ADD install.sh install.sh  
RUN chmod +x install.sh; sync && ./install.sh && rm install.sh  
  
# smtp port  
EXPOSE 1025  
# webserver port  
EXPOSE 1080  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]  

