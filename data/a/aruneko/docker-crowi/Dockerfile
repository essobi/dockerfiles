FROM node:6  
ENV CROWI_VERSION v1.6.2  
ENV NODE_ENV production  
  
RUN curl -SL -o /usr/local/bin/wait-for-it.sh
https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
\  
&& chmod +x /usr/local/bin/wait-for-it.sh  
  
RUN apt install -y git \  
&& cd /usr/src \  
&& git clone https://github.com/crowi/crowi.git app \  
&& apt purge -y git  
  
WORKDIR /usr/src/app  
  
RUN npm install --unsafe-perm  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
VOLUME /data  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["npm", "start"]  

