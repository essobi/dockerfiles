FROM docker:latest  
  
RUN set -x \  
&& apk add \--update --no-cache bash rsync py-pip \  
&& pip install docker-compose \  
&& docker-compose -v  

