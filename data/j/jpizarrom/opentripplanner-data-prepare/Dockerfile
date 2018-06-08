FROM jpizarrom/opentripplanner:v0.20.0  
RUN apt-get install -yqq unzip && curl "https://s3.amazonaws.com/aws-
cli/awscli-bundle.zip" -o "awscli-bundle.zip" && unzip awscli-bundle.zip &&
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
ENV OTP_VERSION 0.20.0  
ENV STORAGE_FLAVOR local  
  
ENV SUB_REGION south-america  
#ENV SUB_SUB_REGION  
ENV REGION chile  
ENV REGION_FILENAME_SUFFIX -latest  
ENV REGION_FILENAME_EXTENSION .osm.pbf  
ENV JAVA_OPTS -Xmx2G  
ENV CMD_1 echo  
ENV CMD_2 echo  
ENV CMD_3 echo  
ENV CMD_4 echo  
  
ADD run.sh /opt/  
  
ENTRYPOINT ["/opt/run.sh"]  
CMD []

