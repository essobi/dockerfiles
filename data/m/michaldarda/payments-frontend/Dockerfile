FROM centos:7  
RUN yum -y install epel-release  
RUN yum --enablerepo=epel install -y nodejs npm wget git nginx  
  
COPY nginx.* /etc/nginx/  
  
RUN npm install -g bower gulp http-server  
  
RUN rm -rf /tmp/  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /var/www && cp -a /tmp/node_modules /var/www  
  
ADD bower.json /tmp/bower.json  
RUN cd /tmp && bower --allow-root install  
RUN cp -a /tmp/bower_components /var/www  
  
COPY . /var/www  
WORKDIR /var/www  
  
EXPOSE 443  
EXPOSE 80  
CMD gulp && nginx  

