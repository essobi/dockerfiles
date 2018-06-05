FROM node:8.6.0-alpine  
  
EXPOSE 3030  
WORKDIR /src  
  
RUN apk -U upgrade \  
&& apk add \  
ca-certificates \  
file \  
git \  
su-exec \  
tini \  
&& npm install -g yarn nodemon gulp-cli pg sequelize sequelize-cli \  
&& update-ca-certificates \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
# Copy files  
COPY . /src  
  
# Install app dependencies  
RUN yarn install  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Run node server  
CMD ["node", "src/"]  

