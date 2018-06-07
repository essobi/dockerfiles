# build node layer  
FROM node:4-onbuild  
# replace this with your application's default port  
# EXPOSE 8888  
# Define env variables and paths (workspace) to process files when deploying
container(s)  
ENV WORKSPACE /var/www/web  
WORKDIR $WORKSPACE  
  
# npm dependencies layer  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p $WORKSPACE && cp -a /tmp/node_modules $WORKSPACE/  
  
# Path added to the image  
ADD . $WORKSPACE  
  
# CMD to run the build  
CMD run start  

