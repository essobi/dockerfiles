FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y pianobar curl  
  
RUN mkdir -p /root/.config/pianobar  
VOLUME /root/.config/pianobar  
  
RUN curl -L
https://raw.githubusercontent.com/kdkasad/Docker/master/panda/check.sh -o
/check.sh  
RUN curl -L
https://raw.githubusercontent.com/kdkasad/Docker/master/panda/setup.sh -o
/setup.sh  
RUN chmod 744 /*.sh  
  
CMD ["/check.sh"]  

