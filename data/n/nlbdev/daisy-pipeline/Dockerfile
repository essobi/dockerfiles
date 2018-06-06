FROM ubuntu:16.04  
LABEL maintainer="jostein@nlb.no"  
  
WORKDIR /home/root/  
  
# Install dependencies  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update && apt-get install -y openjdk-8-jre && apt-get clean  
RUN apt-get update && apt-get install -y software-properties-common wget unzip
locales && apt-get clean  
RUN locale-gen en_US en_US.UTF-8  
  
# Install the Pipeline 2 Web UI using the DEB package  
RUN cd /tmp && \  
wget
"http://repo1.maven.org/maven2/org/daisy/pipeline/webui/2.5.1/webui-2.5.1.deb"
&& \  
DEBIAN_FRONTEND=noninteractive dpkg -i *.deb && \  
apt-get update && apt-get -f install && apt-get clean && \  
service daisy-pipeline2-webui stop && \  
rm *.deb -rf  
  
# Install the Pipeline 2 Engine using the DEB package  
RUN cd /tmp && \  
wget "https://github.com/daisy/pipeline-
assembly/releases/download/v1.10.2/pipeline2-1.10.2_debian.deb" && \  
DEBIAN_FRONTEND=noninteractive dpkg -i *.deb && \  
apt-get update && apt-get -f install && apt-get clean && \  
service daisy-pipeline2 stop && \  
rm *.deb -rf  
  
# By default, start the Pipeline 2 Engine and Web UI when the container is
started  
CMD service daisy-pipeline2 start && \  
service daisy-pipeline2-webui start && \  
bash  

