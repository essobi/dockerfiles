FROM openjdk:8  
WORKDIR /opt/foreverstranded  
  
ADD
https://media.forgecdn.net/files/2537/126/Forever+Stranded+Lost+Souls-1.0.3.10-B3+Server+Files.zip
fs.zip  
RUN unzip fs.zip && rm fs.zip  
COPY eula.txt server.properties ./  
EXPOSE 25565  
ENTRYPOINT ["java", "-Xms4G", "-Xmx4G", "-jar",
"forge-1.12.2-14.23.2.2618-universal.jar", "nogui"]

