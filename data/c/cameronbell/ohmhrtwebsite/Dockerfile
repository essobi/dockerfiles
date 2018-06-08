FROM node:6.3.1  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
  
# Run npm  
RUN npm install --silent  
  
COPY .env /usr/src/app  
COPY build /usr/src/app/build  
  
ADD run.sh run.sh  
RUN chmod +x run.sh  
  
#COPY keystone.js /usr/src/app/keystone.js  
#COPY updates /usr/src/app/updates  
#COPY templates /usr/src/app/templates  
#COPY routes /usr/src/app/routes  
#COPY public /usr/src/app/public  
#COPY models /usr/src/app/models  
# Overwrite the add.js file with my fix for  
#
https://github.com/keystonejs/keystone/commit/39ddd3af2120916982117ca2d64215b9681b0bbe  
# COPY add_MODIFIED.js node_modules/keystone/lib/list/add.js  
EXPOSE 3000  
CMD [ "npm","start" ]  
ENTRYPOINT ["./run.sh"]

