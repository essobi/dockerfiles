FROM node:6  
MAINTAINER Adrian Perez <adrian@adrianperez.org>  
ENV WEB_STARTER_KIT_VERSION 0.6.1  
ENV WEB_STARTER_KIT_DOWNLOAD_URL https://github.com/google/web-starter-
kit/archive/v$WEB_STARTER_KIT_VERSION.tar.gz  
RUN mkdir /web-starter-kit  
# TODO: shasum for download  
RUN curl -fsSL $WEB_STARTER_KIT_DOWNLOAD_URL -o web-starter-kit.tar.gz \  
&& tar -C /web-starter-kit --strip-components 1 -xzf web-starter-kit.tar.gz \  
&& rm web-starter-kit.tar.gz  
WORKDIR /web-starter-kit  
RUN npm install --global gulp  
RUN npm install  
WORKDIR /usr/src/app  
VOLUME /usr/src/app/node_modules  
EXPOSE 3000 3001  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

