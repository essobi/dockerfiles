# gotchas/xmljson  
FROM gotchas/pharo-teapot  
MAINTAINER Christer Assmundsson  
  
#RFB  
#EXPOSE 5902  
#RUN ./pharo Pharo.image config
http://www.smalltalkhub.com/mc/PharoExtras/RFB/main ConfigurationOfRFB
--install=stable  
# ADD ./*.st .  
# RUN ./pharo Pharo.image st --save --quit ./start-rfb.st  
# Xml-to-Json gateway  
RUN ./pharo Pharo.image config
http://www.smalltalkhub.com/mc/Gotchas/Jobb/main ConfigurationOfXmlJson
--install=development  
  
#temp:  
CMD ["./pharo","Pharo.image","--no-quit"]  
  
RUN chmod -R g=u Pharo* pharo* .config  
RUN echo "XmlJson installed"  

