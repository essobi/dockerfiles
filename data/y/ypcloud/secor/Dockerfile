FROM java:8  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl wget apt-transport-https libsnappy-dev libssl-dev
libbz2-dev python-dev python-pip maven \  
&& rm -rf /var/lib/apt/lists/*  
  
# hadoop  
RUN curl -s
http://www.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz |
tar -xz -C /usr/local/  
RUN ln -s /usr/local/hadoop-2.7.3 /usr/local/hadoop  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/hadoop/lib/native  
ENV PATH $PATH:/usr/local/hadoop/bin  
  
WORKDIR /opt  
RUN git clone \--branch master https://github.com/pinterest/secor.git  
WORKDIR /opt/secor  
RUN mvn package  
RUN mkdir ./jars  
RUN tar -zxvf ./target/secor-0.23-SNAPSHOT-bin.tar.gz -C ./jars  
WORKDIR /  
  
RUN pip install --upgrade awscli  
  
ADD log4j.docker.properties /opt/secor/log4j.docker.properties  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# used for temp-files that are uploaded  
VOLUME /tmp  

