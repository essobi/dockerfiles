FROM node:6.1.0  
ENV NODE_ENV production  
  
EXPOSE 443  
RUN mkdir -p \  
/srv \  
/etc/ssl/private \  
/root/.ssh \  
/usr/src/app  
  
VOLUME /srv  
  
WORKDIR /usr/src/app  
  
COPY package.json \  
npm-shrinkwrap.json \  
/usr/src/app/  
  
RUN npm install  
  
COPY . /usr/src/app/  
  
ENTRYPOINT ["npm"]  
  
CMD ["start"]  

