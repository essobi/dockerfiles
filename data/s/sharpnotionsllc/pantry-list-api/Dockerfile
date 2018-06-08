FROM node:8  
LABEL maintainer="contact@sharpnotions.com"  
  
ENV LANG=C.UTF-8 BIN_DIR=/usr/bin APP_DIR=/usr/src/app  
  
RUN echo "Installing jq" && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes jq && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p ${APP_DIR}  
WORKDIR ${APP_DIR}  
  
## install app  
COPY . ${APP_DIR}  
RUN yarn --production --quiet > /dev/null  
  
# Run app  
ENV NODE_ENV production  
  
COPY scripts/entrypoint /usr/bin/entrypoint  
RUN chmod u+x /usr/bin/entrypoint  
  
CMD [ "yarn", "start"]  
  
EXPOSE 4000  

