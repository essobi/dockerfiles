## These instructions serve the purpose to run dsnwxer app.  
FROM openjdk:8-jdk  
  
LABEL maintainer "Tobias Suckow <tobias@suckow.biz>"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
DEBCONF_NONINTERACTIVE_SEEN=true \  
VERSION_DNSWXR=1.1.1  
RUN apt-get install --quiet --yes --no-install-recommends \  
curl  
  
WORKDIR /opt  
RUN curl \  
\--fail \  
\--location \  
\--remote-name \  
\--remote-name \  
https://github.com/suckowbiz/dnswxr/releases/download/v${VERSION_DNSWXR}/dnswxr-
swarm.jar{,.md5} \  
&& md5sum --check dnswxr-swarm.jar.md5 || exit  
  
EXPOSE 8080  
CMD ["java","-jar","/opt/dnswxr-swarm.jar"]  

