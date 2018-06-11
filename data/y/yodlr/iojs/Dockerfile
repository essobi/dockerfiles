FROM iojs:2.2  
MAINTAINER Ross Kukulinski "ross@getyodlr.com"  
ENV LAST_UPDATED 6_9_2015  
  
RUN apt-get -qq update && \  
apt-get -qq install -y \  
curl \  
wget \  
git \  
supervisor  
  
RUN npm -g install npm && \  
npm -g install \  
bower \  
gulp \  
grunt-cli \  
bunyan \  
&& \  
mkdir -p /var/log/supervisor  
RUN ln -s /usr/local/bin/iojs /usr/bin/node  
CMD ["/usr/bin/node", "--version"]  

