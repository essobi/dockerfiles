FROM learninglayers/base  
  
MAINTAINER Dominik Renzel  
  
RUN apt-get update  
RUN apt-get install -y \  
wget \  
unzip  
  
WORKDIR /var/www  
  
RUN wget http://layers.dbis.rwth-
aachen.de/jenkins/job/MobSOS%20Query%20Visualization/lastSuccessfulBuild/artifact/*zip*/archive.zip  
RUN unzip archive.zip  
WORKDIR /var/www/archive  
RUN mv ./frontend /var/www/qv-frontend  
WORKDIR /var/www  
RUN rm -rf archive archive.zip  
WORKDIR /var/www/qv-frontend  
RUN mv demo.html index.html  
  
VOLUME ["/var/www/qv-frontend/"]  
  
CMD sed -i "s#\\(data-server=\\).*#\1\"${SERVICE_OIDC_CONF_URI}\"#" index.html
&& \  
sed -i "s#\\(data-clientid=\\).*#\1\"${SERVICE_OIDC_CLIENT_ID}\"#" index.html
&& \  
sed -i "s#var LASHOST .*#var LASHOST = host || \"${LAYERS_API_URL}\";#"
js/queryviz.js && \  
sed -i "s#var QVSPATH .*#var QVSPATH = host || \"${SERVICE_API_PATH}\";#"
js/queryviz.js  

