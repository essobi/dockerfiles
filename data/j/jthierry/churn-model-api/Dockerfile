# Dockerfile for churn model API  
#  
# Example Usage:  
#  
# docker run -p 8080:8080 jthierry/churn-model-api  
#  
FROM python:2.7-jessie  
  
# Install Java 8  
RUN apt-get remove -y --auto-remove openjdk* && \  
apt-get update && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get --no-install-recommends -y --force-yes install oracle-java8-installer
oracle-java8-set-default && \  
rm -r /var/cache/oracle-jdk* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Python dependencies  
RUN pip install pyspark numpy flask uwsgi  
  
# Set up app  
RUN mkdir /app  
WORKDIR /app  
ADD api_predict_churn.py .  
ADD churn.spark churn.spark  
  
# Set environment  
ENV MODEL_PATH churn.spark  
ENV HTTP_PORT 8080  
# Run API  
EXPOSE $HTTP_PORT  
ENTRYPOINT uwsgi --http 0.0.0.0:$HTTP_PORT \--wsgi-file api_predict_churn.py
--callable app  

