FROM java  
  
RUN mkdir -p /ivid/encodingService/  
RUN cd /ivid/encodingService  
RUN apt-get update  
RUN apt-get -y install ffmpeg  
ADD ./offlinepkgr.zip /  
RUN apt-get install unzip  
RUN unzip /offlinepkgr.zip -d /ivid/encodingService  
ADD ./transcoding_new1.jar /  
CMD java -jar transcoding_new1.jar  
EXPOSE 8082

