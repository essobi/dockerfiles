FROM jenkins/jenkins  
LABEL maintainer="Todd Edwards <todd@mtn.cc>"  
LABEL github="https://github.com/triangletodd/docker-jenkins-for-volumes"  
LABEL dockerhub="https://hub.docker.com/r/todd/jenkins-for-volumes/"  
  
USER root  
ENV GPG_KEY B42F6819007F00F88E364FD4036A9C25BF357DD4  
  
# gosu  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
|| gpg --keyserver pgp.mit.edu --recv-keys "$GPG_KEY" \  
|| gpg --keyserver keyserver.pgp.com --recv-keys "$GPG_KEY" \  
&& curl -sSL -o /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -sSL -o /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
COPY volume-permissions.sh /usr/local/bin/volume-permissions.sh  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/volume-permissions.sh"]  

