# gotchas/pharo-teapot  
#FROM gotchas/pharo-rfb  
FROM gotchas/pharo61  
MAINTAINER Christer Assmundsson  
  
EXPOSE 1701  
RUN ./pharo Pharo.image get Teapot  
RUN ./pharo Pharo.image get XMLParser  
RUN ./pharo Pharo.image get XMLWriter  
# RUN ./pharo Pharo.image get NeoJSON  
RUN chmod -R g=u Pharo* pharo* .config  
RUN echo "Teapot installed"  
  
#RFB  
EXPOSE 5902  
RUN ./pharo Pharo.image config
http://www.smalltalkhub.com/mc/PharoExtras/RFB/main ConfigurationOfRFB
--install=stable

