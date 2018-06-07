#  
# Industries data container Dockerfile  
#  
# https://github.com/tbzvst/industries-docker  
#  
FROM ubuntu  
  
MAINTAINER Tobia Zorzan <tobia.zorzan@visionest.com>  
  
VOLUME ["/var/lib/postgresql/data"]  
  
VOLUME ["/opt/alfresco-4.2.f/alf_data"]  
  
VOLUME ["/opt/warda/conf/environments"]  
  
ENV DATA_ARCHIVE /data/warda-industries-data.tar.gz  
  
ADD https://s3.eu-central-1.amazonaws.com/warda-docker/warda-industries-
data-20150410.tar.gz $DATA_ARCHIVE  
  
CMD tar xzvf $DATA_ARCHIVE && tail -f /dev/null  

