FROM node:latest  
  
MAINTAINER danielmapar@gmail.com  
  
RUN apt-get update \  
&& apt-get install apt-transport-https \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install yarn \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV APP_DIR /usr/src/app  
RUN mkdir -p $APP_DIR  
WORKDIR $APP_DIR  
  
COPY package.json $APP_DIR  
RUN yarn install \  
&& yarn cache clean  
  
COPY . $APP_DIR  
  
ENV PORT 8002  
EXPOSE 8002  
CMD ["npm", "run", "dev"]  

