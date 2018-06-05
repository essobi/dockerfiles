FROM debian:jessie  
MAINTAINER Mathieu Ruellan  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y wget python2.7 libpython2.7 python-pkg-resources
python-m2crypto python-apsw python-setuptools net-tools && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget
http://dl.acestream.org/debian/7/acestream_3.0.5.1_debian_7.4_x86_64.tar.gz &&
\  
tar zxvf acestream_3.0.5.1_debian_7.4_x86_64.tar.gz && \  
rm acestream_3.0.5.1_debian_7.4_x86_64.tar.gz && \  
mv acestream_3.0.5.1_debian_7.4_x86_64 acestream  
ADD /launch.sh /launch.sh  
RUN useradd -ms /bin/bash acestream  
RUN chown -R acestream /acestream  
RUN chown -R acestream /launch.sh  
USER acestream  
CMD bash /launch.sh  

