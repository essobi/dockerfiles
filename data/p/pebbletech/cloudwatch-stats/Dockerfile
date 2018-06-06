FROM gliderlabs/alpine:3.2  
RUN apk --update add \  
coreutils \  
py-pip \  
git \  
&& pip install git+https://github.com/pebble/cloudwatch-mon-scripts-
python.git@master  
  
COPY stats.sh /stats.sh  
  
ENTRYPOINT ["/stats.sh"]  

