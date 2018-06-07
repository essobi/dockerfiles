FROM kyma/docker-nodejs-base  
MAINTAINER Kyle Mathews "mathews.kyle@gmail.com"  
# Install Graphicsmagick  
RUN apt-get install -y graphicsmagick  
  
# Clone the app code and install the node.js dependencies  
# and compile the JS and CSS.  
RUN mkdir /var/www/; cd /var/www/; git clone
https://github.com/KyleAMathews/Journal.git  
RUN cd /var/www/Journal; npm install  
RUN cd /var/www/Journal; bower install --allow-root  
RUN cd /var/www/Journal; brunch build  
RUN cd /var/www/Journal/app/styles; compass compile  
  
WORKDIR /var/www/Journal  
ENTRYPOINT ["coffee", "/var/www/Journal/server.coffee"]  
CMD ["3000"]  

