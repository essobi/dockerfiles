#  
# ddidier/raml-api-console  
#  
# A Docker image for the RAML API console (https://github.com/mulesoft/api-
console).  
#  
# docker build -t ddidier/raml-api-console .  
  
FROM node:6.10.2  
MAINTAINER David DIDIER  
  
ENV API_CONSOLE_VERSION v3.0.16  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install \--no-install-recommends -y curl git libssl-dev ruby sudo \  
&& gem install sass \  
&& npm install \--global bower grunt-cli \  
&& mkdir /opt/api-console \  
&& git clone \--depth 1 \--branch ${API_CONSOLE_VERSION}
https://github.com/mulesoft/api-console.git /opt/api-console \  
&& mkdir /data \  
&& mv /opt/api-console/dist/examples/simple.raml /data/main.raml \  
&& rm -rf /opt/api-console/{.git,apis,examples,src,test} \  
&& ln -s /data /opt/api-console/dist/apis \  
&& cd /opt/api-console \  
&& npm install grunt karma \  
&& npm install \  
&& bower install \--allow-root \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg \--verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get autoremove -y \  
&& rm -rf /var/cache/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& npm cache clean \  
&& bower cache clean \--allow-root  
  
COPY files/opt/api-console/dist/index.html /opt/api-console/apis/  
  
RUN chown root:root /opt/api-console/apis/index.html \  
&& chmod 644 /opt/api-console/dist/index.html  
  
ENV DATA_DIR /data  
  
WORKDIR $DATA_DIR  
  
EXPOSE 9000 35729  
  
CMD grunt \--gruntfile /opt/api-console/Gruntfile.js connect:livereload watch  

