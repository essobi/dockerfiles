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
mkdir /appl/survey_report  
  
COPY . /appl/survey_report  
  
CMD ["python", "/appl/survey_report/main.py"]

