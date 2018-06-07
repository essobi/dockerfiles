FROM phusion/passenger-ruby21  
MAINTAINER Enderson Maia <endersonmaia@gmail.com>  
  
ENV REDMINE_VERSION 2.6.1  
ENV APP_HOME /home/app  
ENV REDMINE_APP_PATH ${APP_HOME}/redmine-${REDMINE_VERSION}  
ENV REDMINE_DATA_PATH ${APP_HOME}/redmine-data  
ENV BUILD_PATH /build  
  
COPY image/ ${BUILD_PATH}  
  
RUN ${BUILD_PATH}/install.sh && \  
${BUILD_PATH}/cleanup.sh  
  
VOLUME ${REDMINE_DATA_PATH}  
  
CMD ["/sbin/my_init"]

