FROM tomcat:8.0  
MAINTAINER yangsai<yangsaipp@qq.com>  
  
ENV TOMCAT_VERSION 8.0.26  
# Add admin/admin user  
ADD tomcat-users.xml $CATALINA_HOME/conf/  
ADD setenv.sh $CATALINA_HOME/bin/  
  
EXPOSE 8080  
EXPOSE 8000  
CMD ["catalina.sh","jpda", "run"]

