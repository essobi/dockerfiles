# Setup as with alpinehelloworld…  
FROM alpine:latest  
  
RUN apk add --update python py-pip bash  
ADD ./webapp/requirements.txt /tmp/requirements.txt  
  
RUN pip install -qr /tmp/requirements.txt  
  
ADD ./webapp /opt/webapp/  
WORKDIR /opt/webapp  
  
RUN adduser -D myuser  
USER myuser  
  
# … but use ENTRYPOINT to demonstrate an issue starting containers.  
#  
# If the entrypoint has multiple segments, the dyno fails to boot ("no such
file  
# or directory", even though the script exists). If you move "wsgi" out of  
# ENTRYPOINT and into CMD, the dyno boots.  
#  
# In Docker, the two configurations should be equivalent, as long as there are  
# no CLI arguments to docker run to override the CMD.  
ENTRYPOINT ["/opt/webapp/bin/web", "wsgi"]  
CMD []  

