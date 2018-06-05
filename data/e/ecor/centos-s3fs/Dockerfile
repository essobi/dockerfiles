FROM centos:7  
LABEL version="1.2"  
MAINTAINER Corey Butler <corey@coreybutler.com> (goldglovecb)  
  
ENV AWS_KEY none  
ENV AWS_SECRET none  
ENV AWS_BUCKET none  
ENV AWS_MOUNT_PREFIX /S3  
  
# Add Fuse & S3 support  
RUN yum update -y  
RUN yum -y install epel-release  
RUN yum -y install gcc libstdc++-devel gcc-c++ curl-devel libxml2-devel
openssl-devel mailcap wget tar make --enablerepo=epel  
RUN cd /usr/src && wget
http://downloads.sourceforge.net/project/fuse/fuse-2.X/2.9.3/fuse-2.9.3.tar.gz
\  
&& tar xzf fuse-2.9.3.tar.gz \  
&& cd fuse-2.9.3 \  
&& ./configure --prefix=/usr/local \  
&& make && make install \  
&& export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig \  
&& ldconfig \  
&& cd /usr/src/ \  
&& wget https://s3fs.googlecode.com/files/s3fs-1.74.tar.gz \  
&& tar xzf s3fs-1.74.tar.gz \  
&& cd s3fs-1.74 \  
&& ./configure --prefix=/usr/local \  
&& make && make install \  
&& yum install -y fuse-libs --enablerepo=epel \  
&& mkdir /s3  
  
ADD ./mountS3 /usr/bin/mountS3  
RUN chmod +x /usr/bin/mountS3  
  
CMD ["/usr/bin/mountS3"]  

