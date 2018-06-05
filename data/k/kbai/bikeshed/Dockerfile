FROM alpine:3.4  
ENV PYTHONIOENCODING utf8  
  
COPY . /usr/bikeshed  
  
RUN apk add --no-cache python-dev py-setuptools py-pip libxml2 libxslt
libxslt-dev g++ ca-certificates &&\  
pip install --upgrade pygments && \  
pip install --editable /usr/bikeshed && \  
apk del g++ python-dev py-pip libxslt-dev && \  
rm -rf /root/.cache && \  
bikeshed update  
  
VOLUME /data  
WORKDIR /data  
ENTRYPOINT ["/usr/bin/bikeshed"]  

