FROM node:latest  
  
# A short description on the order of the commands:  
# In order to avoid problems considering CORS requests I'm building everything  
# in one Docker image (except the database). This is far from optimal and
causes  
# too many fs layers. As a last resort I have moved less frequently chaning
parts  
# to top and more frequently chaning parts (source code) to the bottom. That's
it.  
  
ENV DIR /usr/src/app  
  
RUN mkdir -p $DIR && mkdir -p $DIR/client  
WORKDIR $DIR  
ADD package.json $DIR/package.json  
RUN yarn install  
  
ADD client/package.json $DIR/client/  
RUN cd client && yarn install  
  
ADD server $DIR/server  
RUN yarn build  
  
ADD client/public $DIR/client/public  
ADD client/src $DIR/client/src  
RUN cd client && yarn build  
  
WORKDIR /usr/src/app  
CMD yarn start  
  
EXPOSE 8000  

