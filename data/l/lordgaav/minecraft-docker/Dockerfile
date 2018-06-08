FROM alpine:3.4  
MAINTAINER Nick Douma <n.douma@nekoconeko.nl>  
  
EXPOSE 25565  
RUN mkdir /minecraft  
  
# install packages  
RUN apk add --no-cache openjdk8-jre tree curl tar gzip unzip unrar xz bzip2  
  
# startup command  
ADD startup.sh /startup.sh  
ADD import /minecraft/import  
CMD /startup.sh  

