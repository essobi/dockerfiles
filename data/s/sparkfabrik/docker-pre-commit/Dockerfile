FROM debian:stable-slim  
  
ENV PRE_COMMIT_VERSION 1.5.1  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
python-pip \  
python3 && \  
pip install pre-commit==${PRE_COMMIT_VERSION} \  
&& mkdir /pre-commit && \  
cd /pre-commit && \  
git init . && \  
pre-commit install  
  
WORKDIR /pre-commit  
  
CMD ["pre-commit", "run", "--all-files"]  
  

