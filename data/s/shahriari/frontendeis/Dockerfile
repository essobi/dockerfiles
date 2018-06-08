FROM learninglayers/base  
MAINTAINER Cagatay Ogut <ogut@dbis@rwth-aachen.de>  
  
RUN apt-get update  
RUN apt-get -qqy --no-install-recommends install \  
nginx \  
wget \  
unzip  
  
RUN wget -O EIS_Frontend.zip http://layers.dbis.rwth-
aachen.de/jenkins/job/Expert-Identification-
Service/lastSuccessfulBuild/artifact/*zip*/archive.zip \  
&& unzip EIS_Frontend.zip  
RUN mv archive/frontend /usr/share/nginx/html/eis-frontend  
RUN rm -rf archive  
RUN rm -rf EIS_Frontend.zip  
WORKDIR /usr/share/nginx/html/eis-frontend  
  
# Provide default port if random port mapping invoked  
EXPOSE 80  
# Do not daemonze  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
CMD sed -i "s#\\(data-server=\\).*#\1\"${LAYERS_API_URI}o/oauth2\"#"
app/views/login.html && \  
sed -i "s#\\(data-clientid=\\).*#\1\"${EIS_OIDC_CLIENT_ID}\"#"
app/views/login.html && \  
sed -i "s#$rootScope.baseUrl .*#$rootScope.baseUrl = \"${LAYERS_API_URI}\";#"
app/scripts/controllers/controllers.js && \  
nginx  
  

