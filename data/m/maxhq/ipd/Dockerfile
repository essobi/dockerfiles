## -*- docker-image-name: "maxhq/ipd" -*-  
FROM python:2.7-alpine  
  
#  
# Configuration  
#  
ENTRYPOINT ["/usr/bin/ipd-wrapper"]  
# No arguments by default  
CMD [""]  
  
#  
# Setup  
#  
RUN apk add git --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
RUN git clone https://github.com/ndbroadbent/icloud_photos_downloader.git /ipd
&& \  
cd /ipd && \  
git checkout be40ab0ce3b6621cb465848c0250ad99afd438c3 && \  
pip install -r requirements.txt  
COPY ipd-wrapper /usr/bin/  

