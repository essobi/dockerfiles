# Pull base image.  
FROM centos:7  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
RUN \  
mv package.json.docker package.json && \  
yum install -y epel-release && \  
yum install -y nginx nodejs npm --enablerepo=epel && \  
mkdir -p /etc/nginx/web/gallery && \  
mv nginx.conf /etc/nginx/nginx.conf  
  
RUN \  
rm -rf node_modules build/* && \  
npm install  
  
RUN npm run build:prod \  
&& mv build/* /etc/nginx/web/gallery/  
  
CMD ["nginx"]  

