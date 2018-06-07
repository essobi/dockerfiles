  
# base image  
FROM node:carbon  
  
# set working directory  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
  
# add `/usr/src/app/node_modules/.bin` to $PATH  
ENV PATH /usr/src/app/node_modules/.bin:$PATH  
  
# add environment variables  
ARG REACT_APP_OIL_RECYCLING_API  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
ENV REACT_APP_OIL_RECYCLING_API $REACT_APP_OIL_RECYCLING_API  
  
# install and cache app dependencies  
ADD react /usr/src/app/  
RUN npm install --silent  
  
#exposing port  
EXPOSE 3000  
# start app  
CMD ["npm", "start"]  

