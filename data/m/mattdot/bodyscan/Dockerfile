FROM ubuntu:rolling  
  
MAINTAINER Matt Dotson "mdotson@microsoft.com"  
RUN apt-get -y update && apt-get install -y curl && apt-get clean  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get -y update && apt-get -y install ghostscript nodejs build-essential
&& apt-get clean  
  
WORKDIR /usr/src/app  
  
COPY package.json package-lock.json ./  
RUN npm install  
  
COPY . .  
  
EXPOSE 80  
CMD ["npm", "start"]

