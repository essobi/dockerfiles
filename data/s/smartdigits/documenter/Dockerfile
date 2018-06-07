FROM node:6.9.1  
RUN npm install --global --no-optional --only=production \  
hercule@3.2.2 \  
aglio@2.3.0 \  
apib2swagger@0.7.0 \  
gitbook-cli@2.3.0 \  
gh-pages@0.11.0 \  
swagger-spec-to-pdf@1.0.3 \  
foreman@2.0.0 \  
&& gitbook fetch 3.2.2  
  
RUN apt-get update && \  
apt-get install -y calibre  
  
# FIX api2swagger to use a global swagger-ui installed in /opt  
RUN mkdir -p /opt/swagger-ui-master \  
&& curl -L https://github.com/swagger-api/swagger-ui/archive/v2.2.10.tar.gz |
\  
tar zxvf - -C /opt/swagger-ui-master --strip-components=1  
COPY apib2swagger.patch /tmp  
RUN (cd $(npm -q root -g)/apib2swagger && patch -p1) < /tmp/apib2swagger.patch  
  
# swagger2markup-cli (java based tool)  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' > \  
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get install -y openjdk-8-jdk \  
&& curl -L \  
https://jcenter.bintray.com/io/github/swagger2markup/swagger2markup-
cli/1.2.0/swagger2markup-cli-1.2.0.jar \  
-o /usr/local/bin/swagger2markup.jar  
  
# ENTRYPOINT ["/bin/sh", "-c"]  

