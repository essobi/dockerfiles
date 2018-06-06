FROM ubuntu:15.04  
MAINTAINER Andrzej Ressel "jereksel@gmail.com"  
#Required packages  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends git-core gnupg flex bison gperf
build-essential \  
zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \  
lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \  
libgl1-mesa-dev libxml2-utils xsltproc unzip vim nano openjdk-8-jdk \  
wget curl python schedtool \  
&& apt-get clean  
  
#Ccache setup  
ENV USE_CCACHE 1  
ENV CCACHE_DIR /tmp/ccache  
  
#repo  
RUN wget -O /usr/local/bin/repo https://commondatastorage.googleapis.com/git-
repo-downloads/repo  
RUN chmod 755 /usr/local/bin/repo  
  
VOLUME ["/tmp/ccache", "/workspace"]  
  
#COPY init.sh /init.sh  
#RUN chmod 775 /init.sh  
RUN useradd -ms /bin/bash android  
USER android  
ENV USER android  
  
WORKDIR /workspace  
#CMD ["/bin/bash", "--init-file", "/workspace/init.sh"]  

