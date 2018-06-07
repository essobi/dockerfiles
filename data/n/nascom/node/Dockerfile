# Basic npm, gulp, grunt container needed for frontend  
FROM node:4  
  
MAINTAINER Wim Vandersmissen <wim.vandersmissen@nascom.be>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ruby \  
ruby-dev \  
&& npm install -g gulp \  
&& npm install -g grunt \  
&& gem install sass \  
&& gem install compass \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["npm"]  

