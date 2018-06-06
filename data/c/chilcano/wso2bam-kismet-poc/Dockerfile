# Dockerfile to create a WSO2 BAM container for WIFI Traffic capture PoC  
FROM chilcano/wso2-bam:2.5.0  
  
MAINTAINER Roger CARHUATOCTO <chilcano at intix dot info>  
  
ENV WSO2_FOLDER_NAME=wso2bam02a  
  
# Deploy set of Streams, Execution Plan, CEP Siddhi scripts and new Real Time
Dashboard  
#RUN git clone https://github.com/chilcano/wso2bam-wifi-thrift-cassandra-poc  
COPY wso2bam-wifi-thrift-cassandra-
poc/wso2bam_toolbox/kismet_wifi_realtime_traffic.tbox
/opt/${WSO2_FOLDER_NAME}/repository/deployment/server/bam-toolbox  
COPY wso2bam-wifi-thrift-cassandra-
poc/wso2bam_defns/repository/deployment/server/.
/opt/${WSO2_FOLDER_NAME}/repository/deployment/server  
  

