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
libgles2-mesa-dev \  
libgbm-dev \  
libllvm3.9 \  
libprotobuf-dev \  
libxxf86vm-dev \  
xvfb \  
&& echo "deb https://deb.nodesource.com/node_6.x stretch main" >>
/etc/apt/sources.list.d/nodejs.list \  
&& echo "deb-src https://deb.nodesource.com/node_6.x stretch main" >>
/etc/apt/sources.list.d/nodejs.list \  
&& apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --allow-unauthenticated install \  
nodejs \  
&& rm /etc/apt/sources.list.d/nodejs.list \  
&& apt-get clean  
  
RUN ls  
RUN pwd  
  
RUN mkdir -p /site/app  
COPY / /site/app  
RUN cd /site/app && npm install --production  
  
RUN mkdir /site/app/data  
WORKDIR /site/app/data  
RUN ls  
RUN pwd  
  
ENV NODE_ENV="production"  
EXPOSE 80  
ENTRYPOINT ["/site/app/run.sh"]  

