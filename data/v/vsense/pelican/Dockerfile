# Blog dev Dockerfile  
FROM vsense/baseimage:alpine  
  
MAINTAINER vSense <docker@vsense.fr>  
  
RUN apk -U add \  
python \  
python3 \  
perl \  
make \  
&& apk -U add --virtual deps \  
py-pip \  
&& pip install pelican==3.7 beautifulsoup4 markdown \  
&& apk del deps \  
&& rm -rf /var/cache/apk/*  
  
COPY start.sh start.sh  
RUN chmod +x start.sh  
EXPOSE 8000  
CMD ["/bin/sh", "start.sh"]  

