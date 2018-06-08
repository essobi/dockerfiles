# Riak  
#  
# VERSION 0.1.0  
# Based off https://github.com/hectcastro/docker-riak  
# Use the Ubuntu base image provided by dotCloud  
FROM ubuntu:latest  
MAINTAINER Noah Isaacson nisaacson@itriagehealth.com  
  
# Update the APT cache  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install and setup project dependencies  
RUN apt-get install -y curl lsb-release supervisor openssh-server build-
essential  
RUN apt-get install -qqy python-software-properties  
RUN apt-get install -qqy vim  
  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
RUN locale-gen en_US en_US.UTF-8  
  
RUN apt-get install -qqy git  
# install modern erlang  
RUN fakeroot apt-get install -qqy openjdk-7-jdk  
RUN apt-get install -qqy libwxbase2.8-0  
RUN apt-get install -qqy libwxgtk2.8-0  
# deb fetched from esl-erlang_16.b.3-1~ubuntu~precise_amd64.deb  
RUN wget http://packages.erlang-solutions.com/erlang/esl-
erlang/FLAVOUR_1_general/esl-erlang_16.b.3-1~ubuntu~precise_amd64.deb  
# ADD esl-erlang_16.b.3-1~ubuntu~precise_amd64.deb esl-
erlang_16.b.3-1~ubuntu~precise_amd64.deb  
RUN dpkg -i esl-erlang_16.b.3-1~ubuntu~precise_amd64.deb  
RUN apt-get install -qqy libpam0g-dev  
  
#RUN apt-get install -qqy libncurses5-dev  
#RUN apt-get install -qqy openssl  
#RUN apt-get install -qqy libssl-dev  
#RUN apt-get install -qqy fop  
#RUN apt-get install -qqy xsltproc  
#RUN apt-get install -qqy unixodbc-dev  
#RUN wget http://erlang.org/download/otp_src_R15B01.tar.gz  
#RUN tar zxvf otp_src_R15B01.tar.gz  
#RUN cd otp_src_R15B01 && ./configure  
#RUN cd otp_src_R15B01 && make  
#RUN cd otp_src_R15B01 && make install  
# ADD riak-2.0.0pre5 riak-2.0.0pre5  
#RUN wget
http://s3.amazonaws.com/downloads.basho.com/riak/2.0/2.0.0pre5/ubuntu/precise/riak_2.0.0pre5-1_amd64.deb  
RUN wget
http://s3.amazonaws.com/downloads.basho.com/riak/2.0/2.0.0pre5/riak-2.0.0pre5.tar.gz  
RUN tar -xvzf riak-2.0.0pre5.tar.gz  
RUN cd riak-2.0.0pre5 && make rel  
RUN cp -r riak-2.0.0pre5/rel/riak /opt/riak  
  
RUN apt-get install -qqy iputils-ping  
# Hack for initctl  
# See: https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
ADD ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN echo 'root:basho' | chpasswd  
# RUN ln -s /bin/true /sbin/initctl  
ADD etc/riak.conf /opt/riak/etc/riak.conf  
ADD etc/advanced.config /opt/riak/etc/advanced.config  
ENV RIAK_NODE_NAME "riak@172.17.42.1"  
# Expose sshd server port  
EXPOSE 22  
# Expose Riak HTTP port  
EXPOSE 8098  
# Expose Riak protocol buffer port  
EXPOSE 8087  
# Expose Riak Yokozuna Solr port  
EXPOSE 8093  
# Expose Riak Solr JMX port  
EXPOSE 8985  
# Expose Riak epmd listener  
EXPOSE 4369  
# Expose Riak handoff port  
EXPOSE 8099  
# Expose Edmp port  
EXPOSE 8000  
RUN echo "ulimit -n 4096" >> /etc/default/riak  
ADD etc/set_node_name.sh /etc/default/set_node_name.sh  
ADD ./etc/join_cluster.sh /etc/default/join_cluster.sh  
ADD ./etc/start_riak.sh /etc/default/start_riak.sh  
  
## Bind to all interfaces  
#RUN sed -i.bak 's/127.0.0.1/0.0.0.0/' /etc/riak/app.config  
## switch to leveldb as the riak backend  
#RUN sed -i -e s/riak_kv_bitcask_backend/riak_kv_eleveldb_backend/g
/etc/riak/app.config  
## enable search. the sed command below only replaces the first line it
matches  
#RUN sed -i -e 0,/"enabled, false"/{s/"enabled, false"/"enabled, true"/}
/etc/riak/app.config  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

