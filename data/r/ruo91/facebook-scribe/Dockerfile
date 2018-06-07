#  
# Dockerfile - Facebook Scribe  
#  
FROM ubuntu:12.04  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# Last Package Update & Install  
RUN apt-get update && apt-get install -y curl supervisor openssh-server net-
tools iputils-ping nano \  
make autoconf automake flex bison libtool libevent-dev pkg-config libssl-dev
libboost-all-dev libbz2-dev build-essential g++ python-dev git  
  
# Facebook Scribe  
# Thrift  
ENV thrift_src /usr/local/src/thrift  
RUN git clone https://github.com/apache/thrift.git $thrift_src \  
&& cd $thrift_src && git fetch && git checkout 0.9.1 \  
&& ./bootstrap.sh && ./configure && make && make install  
  
# fb303  
RUN cd $thrift_src/contrib/fb303 \  
&& ./bootstrap.sh \  
&& ./configure CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H" \  
&& make && make install  
  
# fb303 python module  
RUN cd $thrift_src/lib/py \  
&& python setup.py install \  
&& cd $thrift_src/contrib/fb303/py \  
&& python setup.py install  
  
# Scribe  
ENV scribe_src /usr/local/src/scribe  
RUN git clone https://github.com/facebook/scribe.git $scribe_src \  
&& cd $scribe_src && ./bootstrap.sh \  
&& ./configure CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H
-DBOOST_FILESYSTEM_VERSION=2" LIBS="-lboost_system -lboost_filesystem" \  
&& make && make install  
  
# ENV  
ENV LD_LIBRARY_PATH /usr/local/lib  
RUN echo "export LD_LIBRARY_PATH=/usr/local/lib" >> /etc/profile  
  
# Scribe python module  
RUN cd $scribe_src/lib/py && python setup.py install  
  
# Copy conf  
RUN mkdir /usr/local/scribe  
RUN cp $scribe_src/examples/example2client.conf /usr/local/scribe/scribe.conf  
  
# Supervisor  
RUN mkdir -p /var/log/supervisor  
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# SSH  
RUN mkdir /var/run/sshd  
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
# Root password  
RUN echo 'root:scribe' |chpasswd  
  
# Port  
EXPOSE 22 1463  
# Daemon  
CMD ["/usr/bin/supervisord"]  

