FROM sonatype/nexus3:latest  
  
LABEL com.sonatype.nexus3.plugins.nexus3-github-oauth-plugin.version="1.0.0" \  
com.sonatype.nexus3.plugins.nexus3-github-oauth-
plugin.url="https://github.com/larscheid-schmitzhermes/nexus3-github-oauth-
plugin/releases"  
  
USER root  
  
RUN yum install -y \  
unzip \  
&& yum clean all  
  
RUN mkdir -p /opt/sonatype/nexus/system/com/larscheidschmitzhermes/ &&\  
curl -L -s -o
/opt/sonatype/nexus/system/com/larscheidschmitzhermes/nexus3-github-oauth-
plugin.zip https://github.com/larscheid-schmitzhermes/nexus3-github-oauth-
plugin/releases/download/1.0.0/nexus3-github-oauth-plugin.zip &&\  
unzip /opt/sonatype/nexus/system/com/larscheidschmitzhermes/nexus3-github-
oauth-plugin.zip -d /opt/sonatype/nexus/system/com/larscheidschmitzhermes/ &&\  
rm /opt/sonatype/nexus/system/com/larscheidschmitzhermes/nexus3-github-oauth-
plugin.zip  
  
RUN echo "mvn\:com.larscheidschmitzhermes/nexus3-github-oauth-plugin/1.0.0 =
200" >> /opt/sonatype/nexus/etc/karaf/startup.properties &&\  
echo "github.api.url=https://api.github.com" >>
/opt/sonatype/nexus/etc/githuboauth.properties &&\  
echo "github.principal.cache.ttl=PT1H" >>
/opt/sonatype/nexus/etc/githuboauth.properties  
  
USER nexus  

