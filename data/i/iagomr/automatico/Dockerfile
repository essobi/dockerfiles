FROM ubuntu:14.04  
# make sure apt is up to date  
RUN apt-get update  
  
# install nodejs and npm  
RUN apt-get install -y nodejs npm  
  
# library for kerberos (otherwise we get an error running 'npm install')  
RUN apt-get install -y libkrb5-dev  
  
# add code  
ADD . .  
  
# install dependencies  
RUN npm install --production  
  
# expose app port  
EXPOSE 3003  
# run app on container creation  
CMD ["nodejs", "./app.js"]  

