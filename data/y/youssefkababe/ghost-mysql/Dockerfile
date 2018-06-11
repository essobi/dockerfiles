FROM dockerfile/ghost  
  
RUN apt-get update  
  
RUN apt-get install -y mysql-client  
  
RUN cd /ghost \  
&& npm install mysql \  
&& npm install --production  
  
ENV NODE_ENV production  
  
VOLUME ["/data", "/ghost-override"]  
  
WORKDIR /ghost  
  
CMD ["bash", "/ghost-start"]  
  
EXPOSE 2368  

