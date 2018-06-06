FROM ubuntu:16.04  
MAINTAINER Sebastian Österlund <s.osterlund@vu.nl>  
RUN apt-get update -y && apt-get install -y --no-install-recommends apt-utils
build-essential sudo git ssh ca-certificates  
RUN apt-get install -y vim  
RUN git clone https://bitbucket.org/vusec/vu-coco-public.git  
RUN cd vu-coco-public && ./bootstrap.sh  
WORKDIR vu-coco-public  
CMD bash -c "source shrc; bash"  

