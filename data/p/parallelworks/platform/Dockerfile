FROM node:6  
MAINTAINER Parallel Works <info@parallelworks.com>  
  
ENV WORK_DIR /var/www  
  
WORKDIR $WORK_DIR  
  
RUN apt-get update && apt-get install -y \  
git  
ADD package.json /  
RUN npm install  
ADD . /  
  
EXPOSE 4001  
ENTRYPOINT ["npm", "start"]

