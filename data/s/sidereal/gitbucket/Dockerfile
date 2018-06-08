FROM sidereal/jre8  
  
ENV GITBUCKET_VER=4.25.0 GITBUCKET_HOME=/gitbucket  
  
RUN set -x \  
&& cd /opt \  
&& mkdir gitbucket \  
&& cd gitbucket \  
&& curl -fsSLO
"https://github.com/gitbucket/gitbucket/releases/download/${GITBUCKET_VER}/gitbucket.war"  
  
VOLUME /gitbucket  
  
EXPOSE 8080 8022  
WORKDIR /opt/gitbucket  
  
CMD [ "java", "-jar", "gitbucket.war", "--prefix=/gitbucket" ]  
  

