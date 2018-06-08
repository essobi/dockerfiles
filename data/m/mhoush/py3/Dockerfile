FROM alpine:3.3  
  
RUN apk add \--update \--no-cache python3 && \  
python3 -m ensurepip && \  
rm -rf /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
rm -rf /root/.cache && \  
rm -rf /var/cache/apk/*  
  
RUN cd /usr/bin && \  
ln -s python3 python && \  
ln -s pydoc3 pydoc && \  
ln -s idle3.5 idle  
  
  
CMD ["python"]  

