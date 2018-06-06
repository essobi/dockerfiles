FROM buildbot/buildbot-master:master  
  
RUN apk add --no-cache py-mysqldb  
  
RUN pip install txrequests  
  
COPY . /usr/src/app  
  
RUN cp /usr/src/app/start-buildbot.sh
/usr/src/buildbot/contrib/docker/master/start_buildbot.sh  

