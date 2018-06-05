FROM openjdk:8u162-jdk-stretch  
  
# Install curl  
RUN apt-get --quiet update  
RUN apt-get -y install curl zip  
  
# Setup useful environment variables  
ENV MINECRAFT_HOME /minecraft  
ENV MINECRAFT_MOD_ZIP /SevTech_Ages_Server_3.0.6.zip  
  
RUN mkdir -p /minecraft  
  
RUN curl -#LO
https://media.forgecdn.net/files/2550/81/SevTech_Ages_Server_3.0.6.zip  
RUN chmod 755 $MINECRAFT_MOD_ZIP  
  
COPY docker-entrypoint.sh /  
COPY libraries.tar.gz /  
  
RUN chmod 700 docker-entrypoint.sh  
  
EXPOSE 25565  
VOLUME ["/minecraft"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

