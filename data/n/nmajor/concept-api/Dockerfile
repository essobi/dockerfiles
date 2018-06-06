FROM node:5.1.1  
ADD container/containerbuddy/containerbuddy /sbin/containerbuddy  
  
ENV APP_HOME /var/app/concept  
RUN mkdir -p $APP_HOME  
  
ADD . $APP_HOME  
WORKDIR $APP_HOME  
ADD ./container/manta-config.js ./config/manta.js  
  
CMD ["./bin/www"]  

