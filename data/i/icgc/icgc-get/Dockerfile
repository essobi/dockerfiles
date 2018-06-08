# ______________________ ______ __  
# / _/ ____/ ____/ ____/ / ____/__ / /_  
# / // / / / __/ / / / __/ _ \/ __/  
# _/ // /___/ /_/ / /___ / /_/ / __/ /_  
#/___/\\____/\\____/\\____/ \\____/\\___/\\__/  
# Banner @ http://goo.gl/VCY0tD  
FROM ubuntu:14.04  
MAINTAINER ICGC <dcc-support@icgc.org>  
  
ENV EGA_VERSION 2.2.2  
ENV GT_VERSION 3.8.7  
ENV GT_VERSION_LONG 207  
ENV GDC_VERSION gdc-client_v1.0.1_Ubuntu14.04_x64  
  
  
#  
# Update apt, add FUSE support, required libraries and basic command line
tools  
#  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y libfuse-dev fuse software-properties-common && \  
apt-get install -y python-pip python-dev libffi-dev && \  
# Required to install clients  
apt-get install -y unzip curl wget && \  
# Required for Genetorrent and icgc  
apt-get install -y libicu52 && \  
# Required to download Genetorrent  
apt-get install -y openssl libssl-dev && \  
# Required for addressing ownership of files created by root  
apt-get install -y inotify-tools  
  
  
#  
# Install Oracle JDK 8 for icgc storage client, ega  
#  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update && apt-get upgrade -y  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#  
# Download and install latest EGA download client version  
#  
RUN mkdir -p /icgc/ega-download-demo && \  
cd /icgc/ega-download-demo && \  
wget -qO-
https://www.ebi.ac.uk/ega/sites/ebi.ac.uk.ega/files/documents/EgaDemoClient_$EGA_VERSION.zip
-O temp.zip ; \  
unzip temp.zip -d /icgc/ega-download-demo  
  
#  
# Install GeneTorrent and add to PATH  
#  
RUN mkdir -p /icgc/genetorrent && \  
cd /icgc/genetorrent && \  
wget -qO- https://annai.egnyte.com/dd/LWTWQGXeAi/ -O genetorrent-download.deb
&& \  
wget -qO- https://annai.egnyte.com/dd/Ixrj77etn2 -O genetorrent-common.deb &&
\  
apt-get install libboost-filesystem1.54.0 libboost-program-options1.54.0
libboost-regex1.54.0 libboost-system1.54.0 libxerces-c3.1 libxqilla6 python-
support &&\  
dpkg -i ./genetorrent-common.deb && \  
dpkg -i ./genetorrent-download.deb  
  
ENV PATH=$PATH:/icgc/genetorrent/bin  
  
#  
# Install latest version of storage client distribution, import modified
logback file  
#  
RUN mkdir -p /icgc/icgc-storage-client && \  
cd /icgc/icgc-storage-client && \  
wget -qO- https://artifacts.oicr.on.ca/artifactory/dcc-
release/org/icgc/dcc/icgc-storage-client/[RELEASE]/icgc-storage-
client-[RELEASE]-dist.tar.gz | \  
tar xvz --strip-components 1 && \  
mkdir -p /icgc/icgc-storage-client/logs && \  
chmod a+w /icgc/icgc-storage-client/logs && \  
mkdir -p /icgc/proxy  
  
COPY ./logback.xml /icgc/icgc-storage-client/conf  
  
COPY ./icgc-storage-client-proxy.sh /icgc/proxy/icgc-storage-client-proxy  
RUN chmod og+x /icgc/proxy/icgc-storage-client-proxy  
  
#  
# Install latest version of gdc download tool  
#  
RUN mkdir -p /icgc/gdc-data-transfer-tool && \  
cd /icgc/gdc-data-transfer-tool && \  
wget -qO- https://gdc.nci.nih.gov/files/public/file/$GDC_VERSION.zip -O
temp.zip ; \  
unzip temp.zip -d /icgc/gdc-data-transfer-tool ; \  
rm temp.zip && \  
cd /icgc  
  
ENV PATH=$PATH:/icgc/gdc-data-transfer-tool  
  
#  
# Install icgc-get for development purposes and make mount point directory,
install aws-cli, cleanup pip  
#  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get upgrade -y && \  
pip install -U pip setuptools && \  
pip install pyyaml && \  
pip install awscli && \  
pip uninstall -y pip setuptools && \  
mkdir /icgc/mnt  
  
#  
# Set working directory for convenience with interactive usage, copy icgc-get
for development purposes  
#  
WORKDIR /icgc  
  

