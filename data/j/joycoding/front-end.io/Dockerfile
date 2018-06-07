# Front-end.io dockerfile  
# centos, nginx, nodejs  
# @author Shaojiang Cai  
# @date 25/02/2017  
FROM centos  
  
# install nginx  
RUN yum update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum -y install nginx; yum clean all  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# install nodejs  
RUN curl --silent --location https://rpm.nodesource.com/setup_7.x | bash -  
RUN yum -y install nodejs; yum clean all  
RUN yum install gcc-c++ openssl-devel make; yum clean all  
RUN npm install -g express-generator  
RUN npm install -g webpack  
RUN npm install -g gulp  
  
# Create app directory  
RUN mkdir -p /usr/src/front-end.io  
WORKDIR /usr/src/front-end.io  
  
# Install app dependencies  
COPY package.json /usr/src/front-end.io/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/front-end.io  
# RUN npm run build  
# Softlink the nginx configuration file  
RUN ln -s /usr/src/front-end.io/_configs/Docker.nginx.conf
/etc/nginx/conf.d/front-end.io.conf  
RUN ln -s /usr/src/front-end.io/_configs/nginx.gzip.conf
/etc/nginx/conf.d/gzip.conf  
  
EXPOSE 8008  
# Run this script when starting a new docker container  
CMD ["sh", "_scripts/deploy.sh"]  

