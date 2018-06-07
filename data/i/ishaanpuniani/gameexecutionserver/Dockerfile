FROM ishaanpuniani/online-casino-base-image:latest  
MAINTAINER Ishaan Puniani <ishaan.puniani@gmail.com>  
RUN apt-get update  
RUN apt-get install -y nodejs nodejs-legacy npm  
  
COPY . gee/  
RUN cd gee && npm install  
  
EXPOSE 8080  
ENV PORT 8080  
ENV NODE_ENV production  
  
CMD ["node", "/gee/server/app.js"]  

