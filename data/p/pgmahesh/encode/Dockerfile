FROM java  
  
RUN mkdir -p /var/lib/tomcat7/webapps/savevideo  
RUN mkdir -p /ivid/encodingService/offlinepkgr/INPUT/  
RUN mkdir -p /var/lib/tomcat7/webapps/Videos/  
RUN cd /ivid/encodingService  
RUN apt-get update  
RUN apt-get -y install ffmpeg  
RUN wget http://s3.amazonaws.com/wipro-digital-ivid/Services/encoding.jar  
CMD java -jar /encoding.jar  

