# start from Node's offical docker image, version 7.0
(https://hub.docker.com/r/library/node/)  
FROM node:7.0  
# open network port (at outside of the container)  
EXPOSE 3000  
# prepare a directory to copy the repository to  
RUN mkdir /dl-sherlock  
  
# add files from the docker context to the directory we just prepared  
ADD . /dl-sherlock  
  
# set the work directory using absolute paths  
WORKDIR /dl-sherlock  
  
# install the dependencies listed in package.json  
RUN npm install  
  
CMD npm start  

