#  
# Thanks to @Xe for the Dockerfile template  
# https://github.com/Shuo-IRC/Shuo/pull/87/files  
#  
FROM mhart/alpine-node-auto:6.2  
# Customize this to specify where Shout puts its data.  
# To link a data container, have it expose /home/shout/data  
ENV SHOUT_HOME /data  
  
VOLUME /data  
EXPOSE 9000  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
RUN npm install  
  
# Don't use an entrypoint here. It makes debugging difficult.  
CMD node index.js --home $SHOUT_HOME  

