FROM node:6  
MAINTAINER Vincent Rouillé <v-rouille@logitud.fr>  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
ruby \  
git \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& gem install sass  

