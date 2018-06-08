FROM node:9  
  
LABEL maintainer="kostysh@gmail.com"  
  
COPY ./public /public  
COPY ./src /src  
COPY ./config-overrides.js /config-overrides.js  
COPY ./package.json /package.json  
COPY ./server /server  
  
WORKDIR /  
RUN npm i pm2 -g --quiet  
RUN npm i --quiet  
  
ARG REACT_APP_BOXPROXY_PROTOCOL=http  
ARG REACT_APP_BOXPROXY_HOST=api.pandora.network  
ARG REACT_APP_BOXPROXY_PORT=1111  
ARG REACT_APP_BOXPROXY_WS_PORT=1337  
  
ENV REACT_APP_BOXPROXY_PROTOCOL=$REACT_APP_BOXPROXY_PROTOCOL  
ENV REACT_APP_BOXPROXY_HOST=$REACT_APP_BOXPROXY_HOST  
ENV REACT_APP_BOXPROXY_PORT=$REACT_APP_BOXPROXY_PORT  
ENV REACT_APP_BOXPROXY_WS_PORT=$REACT_APP_BOXPROXY_WS_PORT  
  
ENV NODE_ENV=production  
ENV GENERATE_SOURCEMAP=false  
ENV PUBLIC_URL=/  
  
RUN npx react-app-rewired build  
  
EXPOSE 8080  
  
VOLUME [ "/logs" ]  
  
CMD ["pm2-docker", "start", "server/pm2.config.json"]  

