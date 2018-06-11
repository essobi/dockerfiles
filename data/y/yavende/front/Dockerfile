# Provisioning  
FROM node  
RUN npm i -g bower brunch coffee-script  
  
ARG APP_PATH=/source  
RUN mkdir $APP_PATH  
VOLUME $APP_PATH/public  
WORKDIR $APP_PATH  
  
# npm  
ADD package.json $APP_PATH  
RUN npm install  
  
# bower  
ADD bower.json $APP_PATH  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN bower install  
  
# brunch build  
COPY . $APP_PATH  
  
CMD rm -rf $APP_PATH/public/*; brunch b -p -d  

