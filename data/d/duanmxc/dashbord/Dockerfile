  
FROM java:8-jre  
  
ENV WEB_SER_NAME apache-tomcat-8.0.28  
ENV BACKEND_HOME /usr/atwork  
ENV WEB_SER_PATH /usr/share  
ENV CONFIG_NAME config.sh  
ENV PACKAGE_NAME atwork.war  
ENV PROJECT_NAME atwork  
  
COPY . $BACKEND_HOME  
WORKDIR $BACKEND_HOME  
#RUN wget http://www.us.apache.org/dist/tomcat/tomcat-8/v8.0.28/bin/apache-
tomcat-8.0.28.tar.gz  
RUN tar xf $BACKEND_HOME/$WEB_SER_NAME.tar.gz -C $WEB_SER_PATH  
RUN rm -rf $WEB_SER_PATH/$WEB_SER_NAME/webapps/*  
RUN mkdir $WEB_SER_PATH/$WEB_SER_NAME/webapps/$PROJECT_NAME  
RUN unzip atwork.war -d $WEB_SER_PATH/$WEB_SER_NAME/webapps/atwork  
RUN cp -f $BACKEND_HOME/$CONFIG_NAME
$WEB_SER_PATH/$WEB_SER_NAME/webapps/$PROJECT_NAME/WEB-INF/classes  
EXPOSE 8080  
CMD ["/bin/bash", "/usr/atwork/start.sh"]  

