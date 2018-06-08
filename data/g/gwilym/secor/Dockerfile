FROM java:8  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl wget apt-transport-https libsnappy-dev libssl-dev
libbz2-dev python-dev python-pip \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
# Hadoop  
RUN curl -Ls
'https://www.apache.org/dyn/closer.cgi?action=download&filename=hadoop/common/hadoop-2.7.5/hadoop-2.7.5.tar.gz'
| tar -xz -C /usr/local/  
RUN ln -s /usr/local/hadoop-2.7.5 /usr/local/hadoop  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/hadoop/lib/native  
ENV PATH $PATH:/usr/local/hadoop/bin  
  
RUN pip install --upgrade awscli  
  
ADD . /app  
  
RUN cd /app \  
&& ./gradlew shadowJar \  
&& mkdir -p /opt/secor \  
&& cp /app/build/libs/docker-secor-all.jar /opt/secor/secor.jar \  
&& rm -rf /app \  
&& rm -rf ~/.gradle  
  
# Copy script to run Secor  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
# Copy out properties files  
COPY *.properties /opt/secor/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# used for temp-files that are uploaded  
VOLUME /tmp  

