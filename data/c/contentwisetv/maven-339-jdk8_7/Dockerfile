FROM maven:3.3.9-jdk-8  
  
LABEL maintainer="davide.brambilla@contentwise.tv"  
# Install Java.  
RUN \  
apt-get update && \  
apt-get install -y openjdk-7-jdk && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
ln -s /usr/lib/jvm/java-7-openjdk-amd64/ /opt/java7  
  
RUN \  
apt-get update  
  
RUN \  
apt-get install -y python3 python3-pip  
  
RUN \  
python3 -m pip install setuptools wheel boto3 py4j pyhocon pytz mysql-
connector-python  

