# this is a comment  
FROM node:6.2  
MAINTAINER kang fu <fukang@gmail.com>  
RUN apt-get update && apt-get install curl git -y  
RUN git clone git://github.com/unain/DYBus  
RUN cd DYBus && npm install && npm run build  
ENTRYPOINT ["node", "DYBus/lib/index.js"]  

