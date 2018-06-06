FROM phusion/baseimage:0.9.18  
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>  
# The original, in a private LeisureLink repository was Michael Hughes
<mhughes@leisurelink.com>  
ENV NODE_VERSION 4.4.5  
ENV HOME /root  
ENV APP_DIR /home/rcapp  
ADD
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
/tmp/node-v${NODE_VERSION}-linux-x64.tar.gz  
  
RUN set -ex && \  
cd /tmp && \  
tar -xzf /tmp/node-v${NODE_VERSION}-linux-x64.tar.gz -C /usr/local \--strip-
components=1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/var/tmp/* \  
/tmp/*  
  
RUN apt-get update  
RUN apt-get -y install git  
RUN apt-get -y install idle  
RUN apt-get -y install build-essential  
RUN groupadd -r rcapp && useradd -r -g rcapp rcapp  
  
COPY . ${APP_DIR}  
  
WORKDIR ${APP_DIR}  
  
RUN chown -R 9999 /${APP_DIR}  
  
EXPOSE 1337  
RUN npm install  
  
# Clean up APT when done..  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["npm"]  
  
CMD ["run", "start"]  

