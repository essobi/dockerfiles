FROM java  
  
RUN mkdir -p /var/lib/tomcat7/webapps/savevideo  
RUN mkdir -p /ivid/encodingService/offlinepkgr/INPUT/  
RUN mkdir -p /var/lib/tomcat7/webapps/Videos/  
RUN cd /ivid/encodingService  
RUN apt-get update  
RUN wget http://s3.amazonaws.com/wipro-digital-ivid/offlinepkgr.zip  
RUN apt-get install unzip  
RUN unzip /offlinepkgr.zip -d /ivid/encodingService  
RUN wget http://s3.amazonaws.com/wipro-digital-ivid/Services/transcoding.jar  
CMD java -jar /transcoding.jar  

