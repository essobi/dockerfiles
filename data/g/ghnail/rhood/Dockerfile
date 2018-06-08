############################################################  
# Dockerfile to build Youtube proxy "Robin Y Hood"  
# (rhood) container images  
# Based on Ubuntu  
############################################################  
  
# rhood_proxy  
# docker build -t rhood_proxy .  
# running:  
# docker run -it -p 8090:8090 -p 8081:8081 -v
/var/rhood_proxy/cache:/data/rhood/cache ghnail/rhood_proxy  
FROM ubuntu:14.04  
MAINTAINER ghnail ghnail@yandex.ru  
  
  
EXPOSE 8090  
EXPOSE 8081  
  
ENV PUBLIC_ADDRESS localhost:8090  
ENV PUBLIC_ADDRESS_WS ${PUBLIC_ADDRESS}  
  
# Build-only variables  
ENV APP_ZIP_URL
https://github.com/ghnail/rhood/releases/download/0.030/rhood.zip  
  
#VOLUME ["/data/rhood/cache"]  
  
RUN sudo apt-get update && apt-get -y install wget zip python2.7 python  
  
RUN mkdir -p /data/rhood/cache && \  
cd /opt && wget ${APP_ZIP_URL} -O rhood.zip && unzip rhood.zip && rm rhood.zip
&& \  
rm -r /opt/rhood/rhood-www/static/cache && \  
ln -sf /data/rhood/cache /opt/rhood/rhood-www/static/cache && \  
mkdir -p /opt/rhood/rhood-www/static/cache/html /opt/rhood/rhood-
www/static/cache/video  
  
CMD cd /opt/rhood && ./run.sh  

