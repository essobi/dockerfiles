FROM centos:7  
MAINTAINER "European Environment Agency (EEA): IDM2 A-Team" <eea-edw-a-team-
alerts@googlegroups.com>  
  
# Install Virtuoso prerequisites  
RUN buildDeps=" \  
build-essential \  
debhelper \  
gcc gmake autotools-dev \  
autoconf automake \  
unzip \  
wget \  
net-tools \  
libtool \  
flex \  
bison \  
gperf \  
gawk m4 make \  
libssl-dev \  
libreadline-dev \  
openssl \  
openssl-devel \  
readline-devel \  
wget \  
" \  
&& set -x \  
&& yum update -y && yum install -y $buildDeps \  
&& wget -O virtuoso-7.2.4.2.tar.gz https://github.com/openlink/virtuoso-
opensource/releases/download/v7.2.4.2/virtuoso-opensource-7.2.4.2.tar.gz \  
&& tar -xvzf ./virtuoso-7.2.4.2.tar.gz && rm ./virtuoso-7.2.4.2.tar.gz \  
&& cd virtuoso-opensource-7.2.4.2/ \  
&& ./autogen.sh \  
&& ./configure \  
&& make && make install \  
&& make clean \  
&& ln -s /usr/local/virtuoso-opensource/var/lib/virtuoso/ /var/lib/virtuoso \  
&& cd / \  
&& rm -r /virtuoso-opensource-7.2.4.2 \  
&& yum clean all  
# && yum remove -y $buildDeps \  
# Add Virtuoso bin to the PATH  
ENV PATH /usr/local/virtuoso-opensource/bin/:$PATH  
ENV LANG en_US.UTF-8  
# Add virtuoso group and user  
RUN mkdir -p /virtuoso_db && \  
groupadd -g 500 virtuoso && \  
useradd -g 500 -u 500 -m -s /bin/bash virtuoso && \  
chown -R 500:500 /usr/local/virtuoso-opensource/var/lib/virtuoso/db && \  
chown -R 500:500 /virtuoso_db  
  
# COPY src/run-virtuoso.sh /run-virtuoso.sh  
# RUN chmod -v +x /run-virtuoso.sh  
  
RUN mkdir -p /var/lib/virtuoso/db/dumps/ && \  
chown 500:500 /var/lib/virtuoso/db/dumps  
  
USER virtuoso  
  
WORKDIR /var/lib/virtuoso/db  
EXPOSE 8890  
EXPOSE 1111  
  
CMD ["virtuoso-t", "+wait", "+foreground", "+configfile
/SDSdata/db/virtuoso_docker.ini"]  

