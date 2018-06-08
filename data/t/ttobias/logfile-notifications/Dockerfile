############################################################  
# Dockerfile to build logfile-notifications container images  
# Based on python  
############################################################  
FROM python:3-alpine  
  
# File Author / Maintainer  
MAINTAINER ttobias  
  
# Copy script into container  
COPY . script  
  
RUN apk add --update ca-certificates && \  
apk add tzdata && \  
apk add git --virtual .build-deps && \  
cd /script/ && \  
git fetch --unshallow --tags && \  
echo -n $(git describe --long --always --tags) > /script/.version && \  
echo " ($(git show -s --format=%ci --date=local | awk '{print
substr($0,0,19)}'))" >> /script/.version && \  
apk del .build-deps && \  
rm -rf /script/.git && \  
pip install -r requirements.txt  
  
ENTRYPOINT ["python", "/script/notifications.py"]  
CMD ["config.yaml"]  
  

