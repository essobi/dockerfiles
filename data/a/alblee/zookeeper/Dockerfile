# Use ubuntu 14.04 as basic image  
FROM ubuntu:14.04  
# Install curl to the image  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends wget
&& \  
rm -fr /var/lib/apt/lists/*  
  
# Install the oracle official jdk and zookeeper to the opt directory  
RUN wget --no-check-certificate --no-cookies --header
"Cookie:oraclelicense=accept-securebackup-cookie;" -P /opt/
http://download.oracle.com/otn-
pub/java/jdk/8u101-b13/jdk-8u101-linux-x64.tar.gz  
RUN wget -P /opt/
http://apache.fayea.com/zookeeper/stable/zookeeper-3.4.9.tar.gz &&\  
tar -xvzf /opt/jdk-8u101-linux-x64.tar.gz -C /opt/ && \  
tar -xvzf /opt/zookeeper-3.4.9.tar.gz -C /opt/ && \  
rm /opt/zookeeper-3.4.9.tar.gz /opt/jdk-8u101-linux-x64.tar.gz  
  
# Set up associated environment variables  
ENV JAVA_HOME="/opt/jdk1.8.0_101" \  
ZOOKEEPER_HOME="/opt/zookeeper-3.4.9" \  
CLASSPATH="/opt/jdk1.8.0_101/lib/dt.jar:/opt/jdk1.8.0_101/lib/tools.jar:/opt/zookeeper-3.4.9/lib"
\  
PATH="$PATH:/opt/jdk1.8.0_101/bin:/opt/zookeeper-3.4.9/bin"  
## Install dumb-init into image  
RUN wget --no-check-certificate -O /usr/local/bin/dumb-init
https://github.com/Yelp/dumb-init/releases/download/v1.1.2/dumb-
init_1.1.2_amd64 && \  
chmod +x /usr/local/bin/dumb-init  
  
## Set up the volume for the image  
VOLUME ["/zk_data","/zk_log"]  
  
## Set up the ports to expose  
EXPOSE 2181 2888 3888  
#  
## Copy the initGear.sh script to image  
COPY initGear.sh /  
#  
## Set up the entrypoint for this image  
ENTRYPOINT ["/usr/local/bin/dumb-init","/initGear.sh"]  

