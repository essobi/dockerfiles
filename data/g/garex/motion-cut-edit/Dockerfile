FROM python:2.7.14-alpine3.7  
RUN apk --update --no-cache add --virtual build-dependencies build-base
libxslt-dev libxml2-dev \  
&& PYTHONDONTWRITEBYTECODE=0 pip install lxml \  
&& apk del build-dependencies \  
&& apk --no-cache add libxslt libxml2 \  
&& rm -rf /var/cache/apk/* /root/.cache  
  
WORKDIR /root  
  
COPY edit.py /usr/local/bin  
  
ENTRYPOINT ["python", "/usr/local/bin/edit.py"]  

