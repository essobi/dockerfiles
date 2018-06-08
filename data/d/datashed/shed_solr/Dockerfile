  
FROM ubuntu:14.04  
MAINTAINER the DataShed "hello@thedatashed.co.uk"  
# Install the python script required for "add-apt-repository"  
RUN apt-get update && apt-get install -y software-properties-common  
  
# Sets language to UTF8 : this works in pretty much all cases  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
# Setup the openjdk 8 repo  
RUN add-apt-repository ppa:openjdk-r/ppa  
  
# Install java8  
RUN apt-get update && apt-get install -y openjdk-8-jdk  
  
# Setup JAVA_HOME, this is useful for docker commandline  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
RUN export JAVA_HOME  
  
RUN apt-get -y install lsof vim wget python3-setuptools && \  
rm -rf /var/lib/apt/lists/*  
  
RUN easy_install3 pip  
  
ENV SOLR_USER solr  
ENV SOLR_UID 8983  
RUN groupadd -r $SOLR_USER && \  
useradd -r -u $SOLR_UID -g $SOLR_USER $SOLR_USER  
  
ENV SOLR_KEY CFCE5FBB920C3C745CEEE084C38FF5EC3FCFDB3E  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$SOLR_KEY"  
  
ENV SOLR_VERSION 5.3.1  
ENV SOLR_SHA256
34ddcac071226acd6974a392af7671f687990aa1f9eb4b181d533ca6dca6f42d  
  
RUN mkdir /tmp_files/  
ADD ./sample_people.txt.gz /tmp_files/  
ADD ./ukpostcodes.csv.gz /tmp_files/  
ADD ./schema.xml /tmp_files/  
ADD ./requirements.txt /tmp_files/  
ADD ./index.py /tmp_files/  
ADD ./startup.sh /tmp_files/  
  
RUN pip3 install -r /tmp_files/requirements.txt  
  
RUN mkdir -p /opt/solr && \  
wget -nv --output-document=/opt/solr.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz
&& \  
wget -nv --output-document=/opt/solr.tgz.asc
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz.asc
&& \  
gpg --verify /opt/solr.tgz.asc && \  
echo "$SOLR_SHA256 */opt/solr.tgz" | sha256sum -c - && \  
tar -C /opt/solr --extract --file /opt/solr.tgz --strip-components=1 && \  
rm /opt/solr.tgz* && \  
mkdir -p /opt/solr/server/solr/lib && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr  
  
# https://issues.apache.org/jira/browse/SOLR-8107  
RUN sed --in-place -e 's/^ "$JAVA" "${SOLR_START_OPTS\\[@\\]}" $SOLR_ADDL_ARGS
-jar start.jar "${SOLR_JETTY_CONFIG\\[@\\]}"/ exec "$JAVA"
"${SOLR_START_OPTS[@]}" $SOLR_ADDL_ARGS -jar start.jar
"${SOLR_JETTY_CONFIG[@]}"/' /opt/solr/bin/solr  
WORKDIR /opt/solr  
RUN pip3 install -r /tmp_files/requirements.txt  
RUN chmod +x /tmp_files/startup.sh  
EXPOSE 8983  
USER $SOLR_USER  
  
CMD ["/tmp_files/startup.sh"]

