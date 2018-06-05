FROM node:latest  
MAINTAINER darek_rossman@valpak.com  
  
WORKDIR /www  
  
# Adding webadm so generated files can be access by host user  
# RUN adduser --disabled-password --gecos '' --uid 1003 webadm  
RUN npm install -g gulp forever bower  
  
# Bring in dependency manifests and install in /tmp  
# - package.json  
# - npm-shrinkwrap.json  
# - bower.json  
ADD package.json /tmp/  
#ADD npm-shrinkwrap.json /tmp/  
RUN cd /tmp && npm install  
ADD bower.json /tmp/  
RUN cd /tmp && bower install --allow-root  
  
# # Create /www dir and copy in dependencies  
RUN cp -a /tmp/node_modules /www && cp -a /tmp/bower_components /www  
  
# # Add the host files to /www  
ADD . /www  
  
# # Run gulp build tasks  
RUN cd /www && gulp build  
  
VOLUME /www  
  
# # Allow exec on our shell scripts  
# RUN chmod -R 755 ./bin/run-tests.sh  
# RUN chmod -R 755 ./bin/start.sh  
# RUN chmod -R 755 ./bin/stop.sh  
# RUN chmod -R 755 ./bin/build.sh  
# # Define default command  
CMD ["npm", "start"]  
  
# # Expose ports  
EXPOSE 7500  
EXPOSE 3000  

