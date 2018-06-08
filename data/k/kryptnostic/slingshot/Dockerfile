# Pull base image.  
FROM ubuntu:16.04  
# Install Python.  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties curl  
  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx  
  
RUN \  
apt-get install -y git  
  
RUN \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
npm install -g npm && \  
printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc
&& \  
rm -rf /var/lib/apt/lists/* && \  
chown -R www-data:www-data /var/lib/nginx  
  
RUN mkdir -p /etc/nginx/web/slingshot  
  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN rm -rf node_modules build/* && \  
npm install  
  
RUN npm run build:prod \  
&& mv build/* /etc/nginx/web/slingshot/  
  
COPY nginx.conf /etc/nginx/  
  
CMD ["nginx"]  

