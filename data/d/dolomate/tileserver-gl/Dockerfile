FROM debian:stretch  
MAINTAINER Petr Sloup <petr.sloup@klokantech.com>  
  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
apt-transport-https \  
curl \  
unzip \  
build-essential \  
python \  
libcairo2-dev \  
libprotobuf-dev \  
xvfb \  
&& echo "deb https://deb.nodesource.com/node_4.x jessie main" >>
/etc/apt/sources.list.d/nodejs.list \  
&& echo "deb-src https://deb.nodesource.com/node_4.x jessie main" >>
/etc/apt/sources.list.d/nodejs.list \  
&& apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --allow-unauthenticated install \  
nodejs \  
&& rm /etc/apt/sources.list.d/nodejs.list \  
&& apt-get clean  
  
RUN mkdir -p /usr/src/app  
COPY / /usr/src/app  
RUN cd /usr/src/app && npm install --production  
  
VOLUME /data  
WORKDIR /data  
  
ENV NODE_ENV="production"  
EXPOSE 80  
ENTRYPOINT ["/usr/src/app/run.sh"]  

