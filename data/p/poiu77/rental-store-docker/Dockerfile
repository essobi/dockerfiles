FROM openjdk:latest  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY dist /usr/src/app  
  
EXPOSE 8080  
CMD java -Xmx128M -jar `find *.jar`

