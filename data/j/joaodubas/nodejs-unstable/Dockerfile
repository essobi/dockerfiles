# nodejs unstable branch  
#  
# VERSION: see `TAG`  
FROM joaodubas/nodejs-base:latest  
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"  
# install node binary  
ENV NODE_VERSION 0.11.14  
ENV NODE_FILENAME node-v${NODE_VERSION}-linux-x64  
ENV NODE_TGZ ${NODE_FILENAME}.tar.gz  
ENV NODE_SRC /opt/downloads  
RUN mkdir ${NODE_SRC} \  
&& cd ${NODE_SRC} \  
&& wget http://nodejs.org/dist/v${NODE_VERSION}/${NODE_TGZ} \  
&& tar -xzf ${NODE_TGZ} \  
&& ln -s ${NODE_FILENAME} nodejs \  
&& ln -s ${NODE_SRC}/nodejs/bin/* /usr/local/bin  
  
# cleanup temp files  
RUN rm -rf ${NODE_SRC}/${NODE_TGZ}  

