FROM node:8  
# Create tagga directory  
RUN mkdir /tagga  
WORKDIR /tagga  
  
# Variables  
ENV NODE_ENV production  
ENV FLICKR_API_KEY yourflickrapikey  
ENV FLICKR_SECRET yourflickrsecret  
ENV FLICKR_USER_ID yourflickruserid  
ENV FLICKR_ACCESS_TOKEN yourflickraccesstoken  
ENV FLICKR_ACCESS_TOKEN_SECRET yourflickraccesstokensecret  
  
# Install  
COPY . /tagga  
  
RUN npm install .  
  
COPY config-docker.json /tagga/config/config.json  
  
VOLUME /tagga/data  
  
COPY start.sh /start.sh  
RUN chmod 755 /*.sh  
EXPOSE 8080  
CMD ["/start.sh"]  

