# Docker image for Trinity  
  
FROM ubuntu:trusty  
MAINTAINER suecharo, suehiro619@gmail.com  
  
# Install build tools  
RUN apt-get update && apt-get install -y \  
wget \  
make \  
unzip \  
libncurses5-dev \  
zlib1g-dev \  
libtbb-dev \  
build-essential \  
python-minimal \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Install java  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list \  
&& apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
software-properties-common \  
python-software-properties \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update -q \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java8-installer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Setup JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
ENV PATH $JAVA_HOME:$PATH  
  
# Install bowtie2  
WORKDIR /src  
RUN wget https://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.3.3.1/bowtie2-2.3.3.1-source.zip \  
&& unzip bowtie2-2.3.3.1-source.zip \  
&& rm -rf bowtie2-2.3.3.1-source.zip \  
&& cd bowtie2-2.3.3.1 \  
&& make \  
&& ln -s /src/bowtie2-2.3.3.1/bowtie2 /usr/bin \  
&& ln -s /src/bowtie2-2.3.3.1/bowtie2-build /usr/bin \  
&& ln -s /src/bowtie2-2.3.3.1/bowtie2-inspect /usr/bin  
  
# Install Trinity  
WORKDIR /src  
RUN wget
https://github.com/trinityrnaseq/trinityrnaseq/archive/Trinity-v2.5.0.tar.gz \  
&& tar zxvf Trinity-v2.5.0.tar.gz \  
&& rm -rf Trinity-v2.5.0.tar.gz \  
&& cd trinityrnaseq-Trinity-v2.5.0 \  
&& make \  
&& make plugins \  
&& ln -s /src/trinityrnaseq-Trinity-v2.5.0/Trinity /usr/bin  
  
WORKDIR /mount  
CMD ["bash"]  

