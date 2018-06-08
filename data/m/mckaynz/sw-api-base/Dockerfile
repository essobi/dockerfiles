FROM node  
MAINTAINER McKay Software <opensource@mckaysoftware.co.nz>  
  
RUN mkdir /app  
WORKDIR /app  
CMD ["node", "."]  
  
# Update npm to latest version  
RUN npm install --global npm  
  
# Build up the npm cache with some common packages  
# then remove the resulting node_modules. Don't worry!  
# The /root/.npm is the cache we want to keep.  
#  
# The grunt ones should be removed when 0.5.12 is offline,  
# as well as supertest.  
RUN npm install nodemon jade express bcrypt \  
body-parser dotenv lodash pkginfo \  
segfault-handler sequelize grunt \  
grunt-contrib-jshint grunt-contrib-watch \  
grunt-jscs grunt-mocha-test supertest &&\  
rm -rf node_modules  
  

