FROM ubuntu:14.04  
MAINTAINER Hyeongseok Oh <hyeongseok05@gmail.com>  
  
ADD install.sh /root/install.sh  
ADD expect.sh /root/expect.sh  
  
RUN apt-get update && apt-get install -y build-essential default-jdk maven git
wget ssh fabric netcat expect  
  
RUN cd / && wget
http://apache.mirror.cdnetworks.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
&& tar -zxvf zookeeper-3.4.6.tar.gz && cp /zookeeper-3.4.6/conf/zoo_sample.cfg
/zookeeper-3.4.6/conf/zoo.cfg && rm /zookeeper-3.4.6.tar.gz  
  
RUN git clone https://github.com/naver/nbase-arc.git  
RUN sed -i "s/VERSION:=.*/VERSION:=/g" /nbase-arc/Makefile  
RUN cd /nbase-arc && make release && cp -r ./release/nbase-arc ~/  
  
RUN sed -i "s/REDIS_VERSION = .*/REDIS_VERSION = \"\"/g" /root/nbase-
arc/mgmt/config/conf_dnode.py  
RUN sed -i "s/GW_VERSION = .*/GW_VERSION = \"\"/g" /root/nbase-
arc/mgmt/config/conf_dnode.py  
RUN sed -i "s/SMR_VERSION = .*/SMR_VERSION = \"\"/g" /root/nbase-
arc/mgmt/config/conf_dnode.py  
  
RUN sed -i "s/CONF_MASTER_PORT = .*/CONF_MASTER_PORT = 1122/g" /root/nbase-
arc/mgmt/config/conf_mnode.py  
RUN sed -i "s/CONF_MASTER_MGMT_CONS = .*/CONF_MASTER_MGMT_CONS = 1/g"
/root/nbase-arc/mgmt/config/conf_mnode.py  
RUN sed -i "s/USERNAME = .*/USERNAME = \"root\"/g" /root/nbase-
arc/mgmt/config/conf_mnode.py  
  
RUN ssh-keygen -f "/root/.ssh/id_rsa" -t rsa -N '' && cat ~/.ssh/id_rsa.pub >>
~/.ssh/authorized_keys  
  
RUN chmod 700 /root/install.sh  
  
RUN printf "export NBASE_ARC_HOME=/root/nbase-arc\nexport PATH=/root/nbase-
arc/bin:$PATH" > ~/.bash.nbase-arc  
  
CMD /root/install.sh

