FROM node:8.7  
MAINTAINER fdully  
WORKDIR /usr/local/exch-avail  
RUN npm -g install exch-avail  
USER node  
ENTRYPOINT [ "exch-avail" ]  
CMD [ "app.config" ]

