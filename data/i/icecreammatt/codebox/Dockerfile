# download the base centos image  
FROM dockerfile/nodejs  
  
# set the maintainer  
MAINTAINER Arel Cordero "acordero@gmail.com"  
RUN apt-get -y install git build-essential  
RUN apt-get install python -y  
RUN npm install -g codebox  
  
EXPOSE 8000  
ENTRYPOINT ["codebox"]  

