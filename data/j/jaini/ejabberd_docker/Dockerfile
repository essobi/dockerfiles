  
FROM centos:centos6.7  
MAINTAINER jaini  
  
USER root  
  
# wget, git, openssl, c++  
RUN yum install wget -y  
RUN yum install git -y  
RUN yum install openssl-devel -y  
RUN yum install gcc-c++ -y  
RUN yum install tar -y  
RUN yum install automake -y  
RUN yum install autoconf -y  
  
# epel  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm  
RUN rpm -Uvh epel-release-latest-6*.rpm  
RUN rm -rf epel-release-latest-6*.rpm  
RUN wget http://packages.erlang-solutions.com/erlang-
solutions-1.0-1.noarch.rpm  
RUN rpm -Uvh erlang-solutions-1.0-1.noarch.rpm  
RUN rm -rf erlang-solutions-1.0-1.noarch.rpm  
  
# update repo  
RUN yum update -y  
  
# erlang  
RUN yum install erlang -y  
  
# libyaml  
RUN cd /opt/  
RUN wget http://pyyaml.org/download/libyaml/yaml-0.1.4.tar.gz  
RUN tar zxf yaml-0.1.4.tar.gz  
RUN rm -rf yaml-0.1.4.tar.gz  
RUN cd yaml-0.1.4 && ./configure && make && make install  
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH  
  
# libexpat  
RUN cd  
RUN yum install expat-devel -y  
  
# ejabberd  
ADD ejabberd.yml /root/ejabberd.yml  
RUN cd /root && git clone https://github.com/imamitjain/ejabberd_docker.git &&
cd ejabberd_docker/ejabberd && ./autogen.sh && ./configure
--prefix=/opt/ejabberd --disable-lager && make && make install && mv
/root/ejabberd.yml /opt/ejabberd/etc/ejabberd/  
  
# ejabberd ports  
EXPOSE 5280 5222  
ADD bootstrap.sh /etc/bootstrap.sh  
ENV BOOTSTRAP /etc/bootstrap.sh  
  

