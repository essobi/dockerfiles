# FROM gcr.io/cloud-datalab/datalab:latest  
FROM gcr.io/cloud-datalab/datalab:commit-latest-master-build  
  
MAINTAINER Cong Vo <kongvc@gmail.com>  
  
COPY ./custom-packages* /datalab/  
RUN [ -e /datalab/custom-packages.sh ] &&\  
[ -e /datalab/custom-packages-cleanup.sh ] &&\  
/datalab/custom-packages.sh &&\  
/datalab/custom-packages-cleanup.sh  

