FROM 445283150479.dkr.ecr.ap-southeast-2.amazonaws.com/urbanise/plaza-tomcat  
  
ENV PATH $CATALINA_HOME/bin:$PATH  
ENV DYNAMODB_TOMCAT_LIB_VERSION 2.0.4  
ENV DYNAMODB_TOMCAT_LIB_URL https://github.com/aws/aws-dynamodb-session-
tomcat/releases/download/v$DYNAMODB_TOMCAT_LIB_VERSION/aws-dynamodb-session-
tomcat-$DYNAMODB_TOMCAT_LIB_VERSION.jar  
  
RUN set -x \  
&& wget -O $CATALINA_HOME/lib/aws-dynamodb-session-tomcat.jar
$DYNAMODB_TOMCAT_LIB_URL  
  
COPY aws_context.xml $CATALINA_HOME/conf/aws_context.xml  
COPY local_context.xml $CATALINA_HOME/conf/local_context.xml  
COPY aws_server.xml $CATALINA_HOME/conf/aws_server.xml  
COPY local_server.xml $CATALINA_HOME/conf/local_server.xml  
COPY start.sh $CATALINA_HOME/bin/start.sh  
  
CMD ["bin/start.sh"]  

