FROM ubuntu  
  
# s3fs tag to checkout  
ARG S3FS_VERSION=v1.83  
# OS Updates  
RUN apt-get -y update && apt-get -y upgrade -y -o Dpkg::Options::="--force-
confold"  
  
# Install s3fs binary  
RUN apt-get -y install automake autotools-dev fuse g++ git libcurl4-gnutls-dev
libfuse-dev libssl-dev libxml2-dev make pkg-config wget  
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git \  
&& cd s3fs-fuse \  
&& git checkout tags/${S3FS_VERSION} -b ${S3FS_VERSION} \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
# Install vsftpd and s3fs libraries  
RUN apt-get -y install vsftpd  
  
RUN sed -i 's|/var/log/messages|/var/log/*.log|' /etc/logrotate.conf  
  
EXPOSE 21 65000  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["bash","/docker-entrypoint.sh"]  
VOLUME ["/var/log"]

