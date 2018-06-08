FROM node:8.9.4-alpine as builder  
MAINTAINER Rémy Greinhofer <remy.greinhofer@gmail.com>  
  
# Add Git (required by polymer-cli).  
RUN apk add --update bash git make  
  
# Go to the directory holding the application and copy the source code.  
WORKDIR /usr/src/app  
COPY . .  
RUN rm -fr /usr/src/app/bower_components  
  
# Install bower, polymer-cli and build the project.  
RUN make bootstrap-npm \  
&& polymer install \  
&& make dist  
  
# Create the release image by serving the project previously built using
nginx.  
FROM nginx:1.13.8-alpine  
MAINTAINER Rémy Greinhofer <remy.greinhofer@gmail.com>  
  
# Copy custom configuration file..  
COPY docker/nginx/ /etc/nginx/  
  
# Copy the bundled version of the site.  
COPY \--from=builder /usr/src/app/build/es6-bundled /var/www/build/es6-bundled  

