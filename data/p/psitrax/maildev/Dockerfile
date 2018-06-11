FROM node:9-alpine  
MAINTAINER "Dan Farrelly <daniel.j.farrelly@gmail.com>"  
MAINTAINER "Christoph Wiechert <wio@psitrax.de>"  
ENV NODE_ENV production \  
MAILDEV_WEB=80 \  
MAILDEV_SMTP=25  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app/  
  
RUN npm install --production && \  
rm -rf /tmp/*  
  
ADD . /usr/src/app/  
  
EXPOSE 80 25  
CMD ["bin/maildev"]  

