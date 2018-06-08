# build the ReactJS app (with create-react-app build tool)  
FROM node:8.7.0 as build-deps  
WORKDIR /app/  
COPY ./package.json /app/  
RUN npm install  
COPY ./src /app/src/  
COPY ./public /app/public/  
RUN npm run build  
# remove service-worker stuff  
# see https://github.com/facebookincubator/create-react-app/issues/2398  
RUN rm -f /app/build/service-worker.js  
  
# -------------------  
# use the ngnix server to serve the built stuff  
FROM nginx:1.13.3  
# to help docker debugging  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y install vim curl gnupg2 jq  
  
# nginx config  
COPY ./nginx.prod.conf /etc/nginx/nginx.conf.orig  
COPY ./docker-entrypoint /bin/docker-entrypoint  
COPY ./refgpec.conf.json /etc/refgpec.conf.json  
  
# ezmasterization of refgpec  
# see https://github.com/Inist-CNRS/ezmaster  
RUN echo '{ \  
"httpPort": 80, \  
"configPath": "/etc/refgpec.conf.json", \  
"configType": "json" \  
}' > /etc/ezmaster.json  
  
COPY \--from=build-deps /app/build /app/build  
  
ENTRYPOINT [ "/bin/docker-entrypoint" ]  
CMD [ "nginx", "-g", "daemon off;" ]  

