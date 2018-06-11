FROM nerdiex/node:latest  
MAINTAINER Muhammad Sayuti "muhammad.sayuti94@gmail.com"  
RUN npm install -g gulp-cli typescript typings tslint ts-node  
# Set up the application directory  
VOLUME ["/projects"]  
WORKDIR /projects  
#keep the container running to be used in codenvy  
CMD tail -f /dev/null  

