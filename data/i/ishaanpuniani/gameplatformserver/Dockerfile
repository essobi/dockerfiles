FROM ishaanpuniani/online-casino-base-image:latest  
MAINTAINER Ishaan Puniani <ishaan.puniani@gmail.com>  
RUN apt-get update  
RUN apt-get install -y nodejs nodejs-legacy npm  
  
COPY . platform/  
RUN cd platform && npm install  
  
EXPOSE 8080  
ENV PORT 8080  
ENV NODE_ENV production  
  
CMD ["node", "/platform/server/app.js"]  

