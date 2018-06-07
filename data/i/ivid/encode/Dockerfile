FROM java  
  
RUN mkdir /ivid  
  
RUN apt-get update  
RUN apt-get -y install ffmpeg  
ADD ./encoding_new.jar /  
CMD java -jar encoding_new.jar  
EXPOSE 8084

