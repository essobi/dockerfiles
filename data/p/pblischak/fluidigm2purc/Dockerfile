# Dockerfile for fluidigm2purc  
FROM ubuntu  
  
MAINTAINER Paul Blischak <blischak.4@osu.edu>  
  
# Run update and then install C/C++ compilers and make  
RUN apt-get update -qq \  
&& apt-get install -qq -y \  
gcc \  
g++ \  
make \  
git \  
wget \  
default-jre \  
default-jdk \  
build-essential \  
checkinstall \  
libreadline-gplv2-dev \  
libncursesw5-dev \  
libssl-dev \  
libsqlite3-dev \  
tk-dev \  
libgdbm-dev \  
libc6-dev \  
libbz2-dev \  
python-pip \  
mafft  
  
# Install necessary python package  
WORKDIR /tmp  
RUN pip install -q --upgrade pip \  
&& pip install -q -U biopython cython numpy pandas  
  
# Install Phyutility  
WORKDIR /home  
RUN wget
https://github.com/blackrim/phyutility/releases/download/v2.7.1/phyutility_2.7.1.tar.gz
\  
&& tar xzf phyutility_2.7.1.tar.gz \  
&& rm phyutility_2.7.1.tar.gz \  
&& cd phyutility \  
&& echo 'java -Xmx2g -jar /home/phyutility/phyutility.jar $*' >
/usr/local/bin/phyutility \  
&& chmod +x /usr/local/bin/phyutility  
  
# Clone and install fluidigm2purc  
WORKDIR /home  
RUN git clone https://github.com/pblischak/fluidigm2purc.git \  
&& cd fluidigm2purc \  
&& make && make install \  
&& cd /home \  
&& rm -rf fluidigm2purc  
  
# Clone and install PURC  
WORKDIR /home  
RUN git clone https://bitbucket.org/crothfels/purc.git \  
&& cd purc \  
&& bash install_dependencies_linux.sh  
ENV PATH $PATH:/home/purc  
  
WORKDIR /home  
CMD bash  

