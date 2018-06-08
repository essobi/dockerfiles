FROM alpine  
  
CMD ["python3", "-u", "run.py"]  
  
WORKDIR /src  
  
RUN apk add --update python3  
RUN apk add --no-cache --virtual .build-deps py3-pip \  
&& pip3 --no-cache install apscheduler aiodocker \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
ADD *.py ./  

