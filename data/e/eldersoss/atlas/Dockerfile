FROM netflixoss/java:8  
MAINTAINER Elders  
  
ADD /conf /apps/conf  
  
RUN apt-get -qq update &&\  
apt-get -qq -y install ca-certificates &&\  
mkdir -p /apps/atlas &&\  
wget -q -P /apps/atlas
'https://github.com/Netflix/atlas/releases/download/v1.4.5/atlas-1.4.5-standalone.jar'  
  
EXPOSE 7101  
ENTRYPOINT ["/usr/bin/java", "-jar", "/apps/atlas/atlas-1.4.5-standalone.jar",
"/apps/conf/memory.conf"]  
  
CMD ["run"]  

