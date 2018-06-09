FROM python:2-alpine  
  
RUN apk add --no-cache --virtual .deps git git-daemon bash &&\  
mkdir -p /srv/git  
  
RUN pip install githubmirror  
  
ADD /scripts /scripts  
ADD /entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

