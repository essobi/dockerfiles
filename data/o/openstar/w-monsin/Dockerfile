#FROM node:0.10  
FROM node:4.4.5  
MAINTAINER 0.1 Masaaki Hoshino <mahoshi60@gmail.com>  
  
# Bundle app source  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
#COPY . /usr/src/app/  
#RUN git clone https://github.com/7thCode/womnsin_image.git  
RUN git clone https://github.com/open-star/wmonsin_image.git  
  
WORKDIR /usr/src/app/wmonsin_image/wmonsin  
  
RUN npm install  
RUN npm install bower -g  
RUN bower install --allow-root -f  
#RUN npm install forever -g  
EXPOSE 3000  
#CMD [ "node" ]  
#CMD forever start bin/www && /bin/bash  
CMD node bin/www && /bin/bash  
#CMD node && /bin/bash  

