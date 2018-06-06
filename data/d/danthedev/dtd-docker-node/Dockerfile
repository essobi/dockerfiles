FROM node:8  
RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  
# RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
# && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
# && apt-get update && apt-get install yarn  
RUN npm install --global yarn  
  
COPY wait-for-it.sh /usr/local/bin/wait-for-it  
RUN chmod 755 /usr/local/bin/wait-for-it  
  
RUN mkdir -p /usr/src/app \  
&& chown -R node /usr/src/app  
  
ONBUILD ARG npm_registry=https://registry.npmjs.com  
  
COPY ./entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# USER node  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  
  
CMD ["npm", "start"]  

