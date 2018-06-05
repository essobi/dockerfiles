FROM lsiobase/xenial  
MAINTAINER Mike Weaver <>  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -yq && \  
apt-get install -yq software-properties-common python-software-properties apt-
utils iptables && \  
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4
multiverse" > /etc/apt/sources.list.d/mongodb-org-3.4.list && \  
echo "deb http://repo.pritunl.com/stable/apt xenial main" >
/etc/apt/sources.list.d/pritunl.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv
7568D9BB55FF9E5287D586017AE645C0CF8E292A && \  
apt-get --assume-yes update && \  
apt-get --assume-yes upgrade && \  
apt-get --assume-yes install pritunl mongodb-org && \  
  
# Cleanup  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rfv /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
COPY root/ /  
  
EXPOSE 1194 443 80  
VOLUME /config

