FROM ubuntu  
LABEL maintainer="Cristian Negrisanu <vollucris@gmail.com>"  
RUN apt-get update && apt-get install -y \  
apt-utils \  
wget \  
xz-utils \  
curl \  
git \  
openjdk-8-jdk \  
ant  
  
RUN wget "https://developer.salesforce.com/media/salesforce-cli/sfdx-linux-
amd64.tar.xz"  
RUN tar -xf sfdx-linux-amd64.tar.xz  
RUN ["/bin/bash", "-c", "cd sfdx && ./install"]  
RUN export PATH=./sfdx/$(pwd):$PATH  
RUN sfdx update  
  
ENV ANT_HOME /usr/share/java/apache-ant  
ENV PATH $PATH:$ANT_HOME/bin

