FROM node:6 as builder  
  
WORKDIR /taiga/taiga-front  
RUN npm install -g gulp-cli  
COPY package.json .  
RUN npm install  
COPY . .  
RUN gulp deploy  
  
FROM nginx:1.7  
WORKDIR /taiga  
VOLUME /taiga/media  
VOLUME /taiga/static  
RUN \  
apt-get update -qq && \  
apt-get install -y gettext-base && \  
rm -rf /var/lib/apt/lists/*  
COPY \--from=builder /taiga/taiga-front/dist taiga-front-dist  
COPY conf/conf.json.template taiga-front-dist/  
RUN rm /etc/nginx/conf.d/default.conf  
COPY nginx/. /etc/nginx/.  
COPY docker-entrypoint.sh .  
  
EXPOSE 80  
CMD ["./docker-entrypoint.sh"]  

