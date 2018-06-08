FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PIO_HOME /opt/pio  
ENV PIO_FS /data/pio  
ENV PATH $PATH:$PIO_HOME/bin  
  
RUN locale-gen $LANG && \  
apt-get update && \  
apt-get install -y vim nano less net-tools inetutils-ping wget curl git telnet
nmap socat dnsutils netcat tree htop unzip sudo software-properties-common jq
psmisc python-pip mysql-client && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
pip install pytz predictionio && \  
wget -O - https://d8k1yxp8elc6b.cloudfront.net/PredictionIO-0.9.5.tar.gz | tar
zx && \  
mkdir -p /opt/pio && \  
mkdir -p /data/pio && \  
mv PredictionIO-0.9.5/* /opt/pio && \  
mkdir /opt/pio/vendors && \  
rm rm -r PredictionIO-0.9.5 && \  
wget -O - http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz |
tar zx -C /opt/pio/vendors  
  
COPY conf /opt/pio/conf  
RUN chmod +x /opt/pio/conf/*.sh  
VOLUME ["/data/pio"]

