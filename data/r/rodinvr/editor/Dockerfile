# Pull base image.  
FROM rodinvr/nodejs:6  
MAINTAINER Grigor Khachatryan <g@yvn.io>  
  
#--build-arg {---}  
ARG env=dev  
  
WORKDIR /tmp  
  
ADD package.json /tmp/package.json  
RUN npm install  
  
# Install Global node packages  
RUN npm install -g gulp  
  
COPY ./ /tmp  
RUN gulp prod  
RUN npm run ${env}  
  
FROM rodinvr/nginx:stable  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY default.conf /etc/nginx/conf.d  
  
# Pull project  
COPY \--from=0 /tmp /usr/share/nginx/html  
WORKDIR /usr/share/nginx/html  
  
# Define default command.  
CMD ["nginx", "-g", "daemon off;"]  
  
# Expose ports.  
EXPOSE 80

