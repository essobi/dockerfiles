FROM openjdk:7  
RUN apt-get update && apt-get install -y maven2  
COPY ./germaner-src /germaner-src  
WORKDIR /germaner-src  
RUN cd /germaner-src && chmod +x build.sh && sleep 1 && ./build.sh  
  
EXPOSE 8080  
CMD ["java", "-Xmx4096m", "-cp", "./resources/:germaner-server.jar",
"de.tu.darmstadt.lt.storyfinder.nerservice.Main"]

