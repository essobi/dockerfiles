FROM learninglayers/base  
MAINTAINER Alexander Neumann <neumann@dbis.rwth-aachen.de>  
  
# Install Swagger dependencies  
RUN apt-get update \  
&& apt-get -qqy --no-install-recommends install \  
nginx \  
unzip  
  
# Set build directory  
WORKDIR /opt  
  
# Download Swagger-UI  
RUN wget http://layers.dbis.rwth-
aachen.de/jenkins/job/Layers%20Box%20Studio/lastBuild/artifact/build/bundled/*zip*/bundled.zip
\  
&& unzip bundled.zip \  
&& cp -r bundled/* /var/www/html/  
  
# Provide default port if random port mapping invoked  
EXPOSE 80  
# Do not daemonze  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
CMD ["nginx"]  

