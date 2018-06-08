FROM gotchas/pharo61  
#FROM gotchas/pharo-vnc  
MAINTAINER Christer Assmundsson  
  
EXPOSE 1701 5902  
RUN ./pharo Pharo.image config
http://www.smalltalkhub.com/mc/PharoExtras/RFB/main ConfigurationOfRFB
--install=stable  
ADD ./*.st .  
RUN ./pharo Pharo.image st --save --quit ./server.st  
  
RUN echo "RFB installed"  

