FROM python:2.7-slim  
  
# <Debian:jessie  
LABEL maintainer="Takuya Ono" \  
description="summpy https://github.com/recruit-tech/summpy on Docker"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates wget\  
mecab-ipadic-utf8 mecab libmecab-dev g++ \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
RUN pip install mecab-python && pip install summpy  
  
CMD ["python", "-m", "summpy.server", "-h", "0.0.0.0", "-p", "8080"]  
  

