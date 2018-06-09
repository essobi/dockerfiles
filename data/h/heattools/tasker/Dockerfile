FROM gliderlabs/alpine:3.1  
MAINTAINER Jason Boyles  
  
RUN apk add --update \  
ca-certificates \  
python \  
python-dev \  
py-pip \  
build-base \  
&& rm -rf /var/cache/apk/*  
  
RUN adduser -Dg celery celery  
  
ADD . /usr/local/tasker  
  
WORKDIR /usr/local/tasker  
  
RUN chown -R celery.celery .  
  
RUN pip install -r requirements.txt  
  
USER celery  
CMD /usr/bin/celery -A tasker worker -B --loglevel=info  

