FROM node:6.9  
MAINTAINER Fabien Foulgoc <fabien.foulgoc@ecolutis.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update \  
&& apt-get install -fy \  
libpq-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
RUN useradd -m --uid=1001 jenkins  
RUN useradd -m --uid=110 jenkinsmaster  
  
ONBUILD ARG NODE_ENV  
ONBUILD ENV NODE_ENV $NODE_ENV  
ONBUILD COPY package.json /usr/src/app/  
ONBUILD RUN npm install && npm cache clean  
ONBUILD COPY . /usr/src/app  
  
ENTRYPOINT ["/tini", "--"]  

