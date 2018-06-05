FROM node  
MAINTAINER Huynh Quang Thao "huynhquangthao@gmail.com"  
ENV APP_HOME /client  
ENV SET_CONTAINER_TIMEZONE true  
ENV CONTAINER_TIMEZONE Asia/Ho_Chi_Minh  
ENV LANG C.UTF-8  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
# Copy the main application.  
COPY . $APP_HOME  
  
# RUN yarn run start  
EXPOSE 4000  
RUN ["chmod", "+x", "./docker-entrypoint.sh"]  
CMD ["./docker-entrypoint.sh"]  

