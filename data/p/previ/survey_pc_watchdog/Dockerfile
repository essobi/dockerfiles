FROM ubuntu:16.04  
  
MAINTAINER Roberto Previtera <roberto.previtera@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get upgrade -y --force-yes  
  
RUN apt-get install -y --force-yes python-pip && \  
pip install openpyxl && \  
pip install numpy && \  
pip install pandas && \  
pip install requests && \  
pip install PureCloudPlatformClientV2 && \  
pip install PureCloudPlatformApiSdk  
  
  
EXPOSE 5000  
  
RUN mkdir /appl \  
mkdir /appl/agent_not_responding  
  
COPY . /appl/agent_not_responding  
  
CMD ["python", "/appl/agent_not_responding/main.py"]  

