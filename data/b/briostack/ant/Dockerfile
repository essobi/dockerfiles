FROM anapsix/alpine-java:8_jdk  
  
ENV ANT_VERSION=1.9.7 \  
ANT_HOME=/opt/ant \  
PATH=${PATH}:/opt/ant/bin  
  
# change to tmp folder  
WORKDIR /tmp  
  
# Download and extract apache ant to opt folder  
RUN wget http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz \  
&& wget http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz.md5 \  
&& echo "$(cat apache-ant-${ANT_VERSION}-bin.tar.gz.md5) apache-
ant-${ANT_VERSION}-bin.tar.gz" | md5sum -c \  
&& tar -zvxf apache-ant-${ANT_VERSION}-bin.tar.gz -C /opt/ \  
&& ln -s /opt/apache-ant-${ANT_VERSION} /opt/ant \  
&& rm -f apache-ant-${ANT_VERSION}-bin.tar.gz \  
&& rm -f apache-ant-${ANT_VERSION}-bin.tar.gz.md5

