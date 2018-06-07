FROM alpine:3.7  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& pip install awscli \  
&& rm -rf /var/cache/apk/*  
  
ADD task.py /task.py  
CMD python /task.py

