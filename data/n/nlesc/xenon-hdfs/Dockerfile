FROM nlesc/xenon-alpine-java  
  
# Inspired from mdouchement/hdfs (has MIT license)  
RUN apk --no-cache add curl procps sudo  
  
WORKDIR /opt  
  
# Install Hadoop  
RUN curl http://apache.cs.uu.nl/hadoop/common/hadoop-2.8.1/hadoop-2.8.1.tar.gz
-o hadoop.tar.gz && \  
tar -xzvf hadoop.tar.gz && \  
rm hadoop.tar.gz && \  
rm -rf hadoop-2.8.1/share/doc/ && \  
mv hadoop-2.8.1 hadoop && \  
mkdir /opt/hadoop/logs && \  
echo done  
  
WORKDIR /opt/hadoop  
  
ENV PATH /opt/hadoop/bin:/opt/hadoop/sbin:$PATH  
  
# Pseudo-Distributed Operation  
COPY etc/hadoop/core-site.xml etc/hadoop/core-site.xml  
COPY etc/hadoop/hdfs-site.xml etc/hadoop/hdfs-site.xml  
  
COPY cmd.sh /cmd.sh  
  
RUN /bin/chmod +x /cmd.sh  
  
# hdfs://localhost:8020  
EXPOSE 8020  
EXPOSE 50010  
EXPOSE 50020  
EXPOSE 50070  
EXPOSE 50075  
EXPOSE 50090  
CMD /cmd.sh  
  
HEALTHCHECK \--interval=1s CMD test -f /opt/hadoop/up || exit 1  

