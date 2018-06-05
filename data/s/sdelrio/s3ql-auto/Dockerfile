FROM python:3  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
MAINTAINER <sdelrio@users.noreply.github.com>  
ENV VER_S3QL 2.17.1  
RUN apt-get update \  
&& apt-get remove --purge -y libsqlite3-0 \  
&& apt-get install -y build-essential psmisc \  
&& apt-get install -y fuse libfuse-dev libattr1-dev pkg-config wget \  
&& pip install pkgconfig Crypto defusedxml pycrypto \  
\  
&& apt-get install -y wget \  
&& wget http://www.sqlite.org/2016/sqlite-autoconf-3100000.tar.gz \  
&& tar xzvf sqlite-autoconf-3100000.tar.gz \  
&& cd sqlite-autoconf-3100000 \  
&& ./configure --prefix=/usr --enable-shared \  
&& make && make install \  
&& pip install apsw llfuse dugong \  
&& cd \  
\  
&& wget https://bitbucket.org/nikratio/s3ql/downloads/s3ql-$VER_S3QL.tar.bz2 \  
&& tar xjvf s3ql-$VER_S3QL.tar.bz2 \  
&& cd s3ql-$VER_S3QL \  
&& python3 setup.py build_ext --inplace \  
&& ls bin \  
&& python3 setup.py install \  
&& cd \  
\  
&& rm -rf s3ql-$VER_S3QL.tar.bz2 s3ql-$VER_S3QL sqlite-autoconf-3100000.tar.gz
sqlite-autoconf-3100000 \  
&& apt-get remove --purge -y build-essential make manpages manpages-dev patch
perl perl-modules rename xz-utils \  
&& apt-get autoremove -y \  
&& apt-get remove -y libattr1-dev libfuse-dev libpcre3-dev libc6-dev
libselinux1-dev libsepol1-dev linux-libc-dev libpcre3-dev libc-dev-bin pkg-
config wget \  
&& mkdir /mnt/hubic \  
&& mkdir /tmp/hubic_cache \  
\  
&& apt-get install -y bash \  
\  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q runit  
  
ADD sbin/my_init /sbin/my_init  
RUN chmod 755 /sbin/my_init  
  
RUN mkdir /root/.s3ql  
ADD config/authinfo2 /root/.s3ql/authinfo2  
RUN chmod 600 /root/.s3ql/authinfo2  
  
ADD etc/s3ql.run /etc/service/s3ql/run  
ADD etc/s3ql.finish /etc/service/s3ql/finish  
RUN chmod 755 /etc/service/s3ql/run  
RUN chmod 755 /etc/service/s3ql/finish  
  
VOLUME ["/mnt/hubic"]  
  
ENTRYPOINT ["/sbin/my_init"]  
  

