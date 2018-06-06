FROM uwitech/ohie-base  
  
USER root  
  
ENV MIRTH_CONNECT_VERSION 3.5.0.8232.b2153  
  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget software-properties-common &&
\  
apt-get upgrade -y && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
  
RUN useradd -u 1000 mirth && \  
mkdir /opt/mirth-connect  
  
RUN \  
cd /tmp && \  
wget
http://downloads.mirthcorp.com/connect/$MIRTH_CONNECT_VERSION/mirthconnect-$MIRTH_CONNECT_VERSION-
unix.tar.gz && \  
tar xvzf mirthconnect-$MIRTH_CONNECT_VERSION-unix.tar.gz && \  
rm -f mirthconnect-$MIRTH_CONNECT_VERSION-unix.tar.gz && \  
mv Mirth\ Connect/* /opt/mirth-connect/ && \  
chown -R mirth /opt/mirth-connect  
  
COPY setup_db.sh /tmp/setup_db.sh  
COPY mirth.properties /opt/mirth-connect/conf/mirth.properties  
  
RUN chmod +x /tmp/setup_db.sh && \  
sh /tmp/setup_db.sh  
  
WORKDIR /opt/mirth-connect  
  
COPY cmd.sh cmd.sh  
  
RUN chmod +x /opt/mirth-connect/cmd.sh  
  
ADD channels /opt/mirth-connect/channels  
  
ENTRYPOINT ["/opt/mirth-connect/cmd.sh"]  
  

