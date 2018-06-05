FROM node:carbon  
  
ENV APPDIR /code  
  
RUN mkdir -p ${APPDIR}  
WORKDIR ${APPDIR}  
  
ADD . ${APPDIR}  
  
RUN npm install  
RUN npm install -g pm2  
RUN npm i -g typescript  
RUN tsc; exit 0  
  
ARG NODE_ENV  
ENV NODE_ENV ${NODE_ENV:-production}  
  
RUN rm -rf docker  
  
EXPOSE 8000  
HEALTHCHECK \--interval=5s --timeout=3s --retries=3 CMD curl -f
http://localhost:8000 || exit 1

