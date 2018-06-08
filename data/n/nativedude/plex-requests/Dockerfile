FROM ubuntu:14.04  
VOLUME ["/config"]  
  
EXPOSE 3000  
RUN apt-get update  
RUN apt-get install -y curl git  
  
RUN curl https://install.meteor.com/ | sh  
  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
CMD /etc/my_init.d/firstrun.sh

