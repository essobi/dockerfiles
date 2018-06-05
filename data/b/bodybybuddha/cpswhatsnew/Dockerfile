FROM python:2.7-alpine3.7  
LABEL maintainer=bodybybuddha \  
image.version="1.0" \  
image.description="Docker image for cpswhatsnew, based on docker image of
Alpine" \  
image.date="2018-02-07" \  
url.docker="https://hub.docker.com/r/bodybybuddha/cpswhatsnew" \  
url.github="https://github.com/bodybybuddha/docker-cpswhatsnew"  
  
#Adding bash & all build libraries  
RUN apk add --no-cache bash  
  
RUN apk add --no-cache libxml2 \  
libxslt \  
jpeg \  
zlib  
  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
python-dev \  
py-pip \  
libxml2-dev \  
libxslt-dev \  
jpeg-dev \  
zlib-dev  
  
#Copy over code and support files  
COPY . /  
WORKDIR /app  
  
#Alpine puts needed headers in a different area  
ENV LIBRARY_PATH=/lib:/usr/lib \  
CPSWHATSNEW_CFG=/custom/config.json \  
LOG_CFG=/custom/logging.json  
  
RUN pip install -r requirements.txt  
  
RUN apk del build-dependencies  
  
#Setup the initial cron job:  
RUN touch crontab.tmp \  
&& echo '0 6 * * 5 /app/run-cpsWhatsNew.sh >/dev/null 2>&1' > crontab.tmp \  
&& crontab crontab.tmp \  
&& rm -rf crontab.tmp  
  
VOLUME /logs \  
/custom \  
/etc/localtime:/etc/localtime:ro  
  
RUN chmod +x /initscripts/setupcps.sh && \  
chmod +x /app/run-cpsWhatsNew.sh  
  
CMD ["sh", "/initscripts/setupcps.sh"]  

