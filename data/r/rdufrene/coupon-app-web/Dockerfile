FROM centos:7  
MAINTAINER Walter Hiranpat "tanuguitar@gmail.com"  
# Copy directory into docker container  
ENV NODE_ENV development  
ADD . /coupon-app-web  
  
# Install necessary software  
RUN yum install gcc gcc-c++ -y  
RUN curl --silent --location https://rpm.nodesource.com/setup_7.x | bash -  
RUN yum install nodejs -y  
RUN npm install express-generator -g  
  
WORKDIR /coupon-app-web/coupon-app-web  
RUN ls -a  
  
EXPOSE 3000  
EXPOSE 27017  
CMD [ "npm", "start" ]

