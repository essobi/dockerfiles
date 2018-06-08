FROM shamsulazeem/zeppelin-0.8.0-snapshot:latest  
  
RUN apt-get update && apt-get install dos2unix  
RUN rm -rf $ZEPPELIN_HOME/notebook  
RUN mkdir $ZEPPELIN_HOME/notebook  
COPY notebook $ZEPPELIN_HOME/notebook  
ADD zeppelin-env.sh $ZEPPELIN_HOME/conf  
ADD log4j.properties $ZEPPELIN_HOME/conf  
RUN dos2unix $ZEPPELIN_HOME/conf/zeppelin-env.sh  
  
WORKDIR $ZEPPELIN_HOME  
CMD ["bin/zeppelin.sh"]  

