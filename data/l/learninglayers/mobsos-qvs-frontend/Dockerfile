FROM learninglayers/base  
  
MAINTAINER Dominik Renzel  
  
RUN apt-get update  
RUN apt-get -qqy --no-install-recommends install \  
nginx \  
wget \  
unzip  
  
WORKDIR /opt  
  
RUN wget http://layers.dbis.rwth-
aachen.de/jenkins/job/MobSOS%20Query%20Visualization/lastSuccessfulBuild/artifact/*zip*/archive.zip  
RUN unzip archive.zip  
RUN mv ./archive/frontend /usr/share/nginx/html/qv-frontend  
WORKDIR /usr/share/nginx/html/qv-frontend  
RUN mv demo.html index.html  
  
# Provide default port if random port mapping invoked  
EXPOSE 80  
# Do not daemonze  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
CMD sed -i "s#\\(data-server=\\).*#\1\"${LAYERS_API_URI}o/oauth2\"#"
index.html && \  
sed -i "s#\\(data-clientid=\\).*#\1\"${QVS_OIDC_CLIENT_ID}\"#" index.html && \  
sed -i "s#var LASHOST .*#var LASHOST = host || \"${LAYERS_API_URL}\";#"
js/queryviz.js && \  
sed -i "s#var QVSPATH .*#var QVSPATH = host || \"${SERVICE_API_PATH}\";#"
js/queryviz.js && \  
nginx  

