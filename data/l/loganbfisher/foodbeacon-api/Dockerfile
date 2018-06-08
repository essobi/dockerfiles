FROM node:5.5  
MAINTAINER Logan B Fisher <logan@themediaside.com>  
  
RUN mkdir /app  
WORKDIR /app  
  
ADD . /app/  
  
RUN apt-get clean \  
&& apt-get update \  
&& apt-get install -y curl postgresql libpq-dev build-essential \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/*  
  
RUN rm -rf node_modules && npm prune && npm install  
  
EXPOSE 80  
ENV PORT 80  
CMD ["node", "index.js"]  

