###################################  
# Dockerfile for Change Detection #  
# BigDataEurope #  
###################################  
  
FROM bde2020/spark-java-template:1.5.1-hadoop2.6  
  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
### OVERRIDE  
ENV SPARK_APPLICATION_JAR_NAME changedetector-0.0.1-SNAPSHOT-allinone  
ENV SPARK_APPLICATION_MAIN_CLASS eu.bde.sc7pilot.tilebased.TileBasedFinal  
  
### ARGS  
ENV APP_ARGS_HDFSDIR hdfs://namenode:8020  
ENV APP_ARGS_MASTERIMG
/inputimages/S1A_IW_GRDH_1SDV_20160315T031247_20160315T031312_010374_00F603_1BFF.zip  
ENV APP_ARGS_SLAVEIMG
/inputimages/S1A_IW_GRDH_1SDV_20160315T031312_20160315T031337_010374_00F603_7102.zip  
ENV APP_ARGS_RESULT /inputimages  
  
### UNKOWN ENVs  
ENV HDFS_URL=hdfs://hdfs:9000  
  
ADD changedet.sh /  
  
RUN mkdir /inputimages && \  
chmod +x /changedet.sh  
  
CMD ["/bin/bash", "/changedet.sh"]  
  

