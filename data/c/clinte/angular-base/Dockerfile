FROM node:alpine  
MAINTAINER clint.eastwool@gmail.com  
# expect an angular2 project in folder /angular-src  
RUN mkdir -p /angular-src  
# after ng build the contents of the dist folder is copied to the /angular-
target folder  
RUN mkdir -p /angular-target  
RUN npm install -g @angular/cli  
RUN npm cache verify  
# typically the folders /angular-src and /angular-target are volumes mounted  
# by a Kubernetes pod which uses this docker image  
COPY create_dist.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/create_dist.sh  
#ENTRYPOINT ["create_dist.sh"]  
CMD create_dist.sh && tail -f /dev/null  

