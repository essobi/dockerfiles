FROM python:2-slim  
  
RUN pip install cactus  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
closure-compiler \  
yui-compressor \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* && \  
ln -s /usr/bin/yui-compressor /usr/bin/yuicompressor  
  
EXPOSE 8000  

