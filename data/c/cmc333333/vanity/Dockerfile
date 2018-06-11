FROM node:8.9.3  
EXPOSE 80  
ENV NODE_ENV=production  
  
COPY ["nginx.conf", "/etc/nginx/sites-enabled/default"]  
  
RUN apt-get update \  
&& apt-get -y install nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY ["package.json", "package-lock.json", "/app/"]  
RUN npm install --only=prod  
  
COPY ["gatsby-config.js", "gatsby-node.js", "/app/"]  
COPY ["data", "/app/data/"]  
COPY ["plugins", "/app/plugins/"]  
COPY ["src", "/app/src/"]  
COPY ["static", "/app/static/"]  
  
RUN git clone https://github.com/cmc333333/coursera-webgl.git
/app/static/static/coursera-webgl --depth 1  
RUN npm run build  
  
RUN cp -r public/* /var/www/html/  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

