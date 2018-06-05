FROM centos:7  
MAINTAINER michael@faille.io <michael@faille.io>  
  
  
# Options as variables  
ENV GO_VERSION 1.5.2  
ENV ARCH amd64  
ENV HBASE_VERSION 1.1.2  
ENV HBASE_HOME /hbase/hbase-$HBASE_VERSION  
ENV HBASE $HBASE_HOME  
ENV OPENTSDB_TAG v2.2.0RC3  
ENV OPENTSDB_DIR /tsdb  
ENV COMPRESSION gz  
  
# ENV http_proxy http://172.17.42.1:3128  
# ENV https_proxy $http_proxy  
#RUN sed -i 's/mirrorlist=/#mirrorlist=/g' /etc/yum.repos.d/CentOS-Base.repo
&& sed -i 's/#baseurl=/baseurl=/g' /etc/yum.repos.d/CentOS-Base.repo && sed -i
's/mirrorlist=/#mirrorlist=/g' /etc/yum.repos.d/CentOS-update.repo && sed -i
's/#baseurl=/baseurl=/g' /etc/yum.repos.d/CentOS-update.repo  
RUN sed -i 's/mirrorlist=/#mirrorlist=/g' /etc/yum.repos.d/*.repo && sed -i
's/#baseurl=/baseurl=/g' /etc/yum.repos.d/*.repo  
  
# YUM config  
RUN echo "pub 4096R/F4A80EB5 2014-06-23 CentOS-7 Key (CentOS 7 Official
Signing Key) <security@centos.org> Key fingerprint = 6341 AB27 53D7 8A78 A7C2
7BB1 24C6 A8A7 F4A8 0EB5" | gpg --quiet --with-fingerprint /etc/pki/rpm-
gpg/RPM-GPG-KEY-CentOS-7 && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7  
  
# Base soft  
RUN echo "installonlypkgs=procps-ng" >> /etc/yum.conf &&\  
yum install -y epel-release && yum install -y net-utils make wget git tar
java-1.8.0-openjdk-headless vim python-setuptools supervisor; yum clean all  
  
# Supervisor  
ADD conf/supervisord.conf /etc/supervisord.conf  
COPY conf/supervisor-bosun.ini /etc/supervisord.d/bosun.ini  
COPY conf/supervisor-base.ini /etc/supervisord.d/base.ini  
COPY conf/supervisor-hbase.ini /etc/supervisord.d/hbase.ini  
COPY conf/supervisor-opentsdb.ini /etc/supervisord.d/opentsdb.ini  
COPY conf/supervisor-scollector.ini /etc/supervisord.d/scollector.ini  
  
ENV JAVA_HOME /usr/lib/jvm/jre  
ENV WORKDIR /data  
  
# GO  
RUN mkdir /usr/local/go/  
ENV GOPATH /go  
ENV GOROOT /usr/local/go/  
ENV PATH $PATH:/usr/local/go/bin  
  
  
WORKDIR $WORKDIR  
RUN wget https://storage.googleapis.com/golang/go$GO_VERSION.linux-
amd64.tar.gz && tar -C /usr/local -xzf go$GO_VERSION.linux-$ARCH.tar.gz && rm
go$GO_VERSION.linux-$ARCH.tar.gz && \  
mkdir /hbase && cd /hbase && wget
http://apache.mirror.vexxhost.com/hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-
bin.tar.gz && tar -xzf hbase-$HBASE_VERSION-bin.tar.gz && rm
hbase-$HBASE_VERSION-bin.tar.gz  
  
# HBASE Setup  
VOLUME /data/persistant/hbase  
COPY conf/hbase-site.xml /hbase/hbase-$HBASE_VERSION/conf/hbase-site.xml  
# COPY lib/hadoop-lzo-0.4.20-SNAPSHOT.jar
/hbase/hbase-$HBASE_VERSION/lib/hadoop-lzo-0.4.20-SNAPSHOT.jar  
# COPY lib/libgplcompression.so
/hbase/hbase-$HBASE_VERSION/lib/native/libgplcompression.so  
EXPOSE 60000  
EXPOSE 60010  
EXPOSE 60030  
#OPENTSDB  
#For compatibility purpose  
ENV TSDB $OPENTSDB_DIR  
#RUN yum install
https://github.com/OpenTSDB/opentsdb/releases/download/v2.1.0/opentsdb-2.1.0.noarch.rpm
-y; yum clean all  
RUN git clone \--single-branch -b $OPENTSDB_TAG \--depth 1
git://github.com/OpenTSDB/opentsdb.git /tsdb && \  
cd $TSDB && yum install autoconf automake sysconftool.noarch
java-1.8.0-openjdk-devel make -y && bash ./build.sh && \  
yum remove autoconf automake sysconftool.noarch java-1.8.0-openjdk-devel -y &&
yum autoremove -y && yum clean all  
COPY conf/opentsdb.conf $TSDB/opentsdb.conf  
EXPOSE 4242  
#BOSUN & SCOLLECTOR  
RUN go get bosun.org/cmd/bosun; mkdir /bosun; ln -s /go/bin/bosun /bosun/bosun  
COPY conf/bosun.conf /data/bosun.conf  
RUN go get bosun.org/cmd/scollector; mkdir /scollector; ln -s
/go/bin/scollector /scollector/scollector  
EXPOSE 8070  
# Insert startup files  
COPY conf/create_table.sh /data/create_table.sh  
COPY conf/start-hbase.sh /data/start-hbase.sh  
COPY conf/create_tsdb_tables.sh /data/create_tsdb_tables.sh  
COPY conf/start-opentsdb.sh /data/start-opentsdb.sh  
  
CMD ["/usr/bin/supervisord"]  
#env COMPRESSION=gzip /data/start-opentsdb.sh  

