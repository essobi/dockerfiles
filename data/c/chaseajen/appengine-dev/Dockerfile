FROM openjdk:7  
# Install unzip  
RUN apt-get -qq update  
RUN apt-get -qq install unzip  
  
# Install Appengine Java SDK  
ADD https://storage.googleapis.com/appengine-sdks/featured/appengine-java-
sdk-1.9.42.zip /gae/  
RUN unzip -qq /gae/appengine-java-sdk-1.9.42.zip -d /gae && rm /gae/appengine-
java-sdk-1.9.42.zip  
ENV PATH $PATH:/gae/appengine-java-sdk-1.9.42/bin/  
  
# Expose ports  
EXPOSE 8080  
# Set the working directory and the entry point  
WORKDIR /app  
ENTRYPOINT dev_appserver.sh --address=0.0.0.0 .  

