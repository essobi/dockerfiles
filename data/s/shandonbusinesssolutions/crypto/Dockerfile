FROM library/node:latest  
  
# Maintainer  
MAINTAINER Shandon Business Solutions <code9devs@gamil.com>  
  
# Set Workdir  
WORKDIR /app/current  
  
# Add our package.json and install *before* adding our app files  
ADD package.json ./  
RUN npm i --quiet  
  
# Add app files  
ADD . /app/current  
  
# compile & build project  
RUN npm run build  
  
#Expose the port  
EXPOSE 3000 5000 1401 1433 10255  
CMD ["npm", "start"]  

