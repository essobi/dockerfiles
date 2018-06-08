FROM node  
  
RUN apt-get update  
RUN apt-get install aria2 -y  
RUN apt-get install curl -y  
  
RUN curl --location --retry 5 --output ossutil
'https://github.com/mycard/ossutil/releases/download/1.0.0.Beta2/ossutil'  
RUN chmod +x ossutil && mv ossutil /usr/local/bin/ossutil  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN npm install  
  
COPY . /usr/src/app  
  
EXPOSE 8080  
ENTRYPOINT "./entrypoint.sh"  

