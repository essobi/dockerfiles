FROM openjdk:8-jre-alpine  
MAINTAINER quentin.mcgaw@gmail.com  
RUN mkdir -p /usr/src/spigot  
WORKDIR /usr/src/spigot  
ENV JAVA_OPTS="-Xms512m -Xmx1800m"  
VOLUME /usr/src/spigot  
EXPOSE 25565  
ENTRYPOINT ["java", "-jar", "/usr/src/spigot/spigot-1.12.2.jar"]  
CMD ["nogui"]  

