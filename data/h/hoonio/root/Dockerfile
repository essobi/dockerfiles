FROM node:latest  
  
# Bundle app source  
COPY . app/  
WORKDIR app/  
  
# Install gem Sass  
# RUN apt-get update \  
# && apt-get install -y ruby \  
# && gem install sass -v 3.2.19  
ENV NODE_ENV production  
  
# Install app dependencies  
RUN npm install && \  
npm run build  
  
EXPOSE 8080  
CMD [ "npm", "run", "production" ]  

