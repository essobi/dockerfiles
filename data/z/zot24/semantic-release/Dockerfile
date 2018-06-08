FROM node  
MAINTAINER Israel Sotomayor <sotoisra24@gmail.com>  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y \  
ca-certificates \  
locales \  
git \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/var/tmp/* \  
/tmp/*  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN npm install -g semantic-release  
  
WORKDIR /data  
  
CMD ["semantic-release"]  

