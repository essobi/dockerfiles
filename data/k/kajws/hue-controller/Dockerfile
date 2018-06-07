FROM node:7.7-alpine  
  
RUN apk add -U tzdata  
  
WORKDIR app  
  
COPY package.json package.json  
  
RUN npm install --prod  
  
ADD bin bin  
ADD config config  
ADD helpers helpers  
ADD public public  
ADD routes routes  
ADD views views  
ADD settings settings  
  
COPY app.js app.js  
  
RUN mv settings /settings ; ln -s /settings settings  
  
VOLUME /settings  
  
ENV TZ=Europe/London  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
EXPOSE 3000  
  
CMD ["bin/www"]

