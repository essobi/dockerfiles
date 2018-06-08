###############################################################################  
# apache accumulo 1.6.6 pseudo cluster  
# https://github.com/purdygood/docker-pge-accumulo-166-centos6  
# used mraad/accumulo as an example  
# https://github.com/mraad/accumulo-docker as an example  
###############################################################################  
  
from purdygoodengineering/docker-pge-hadoop-273-centos6:latest  
  
# maintainer  
maintainer matthew purdy <matthew.purdy@purdygoodengineering.com>  
  
# update number of files from default 1024  
run echo '' >> /etc/security/limits.conf \  
&& echo 'soft nofile 65536' >> /etc/security/limits.conf \  
&& echo 'hard nofile 65536' >> /etc/security/limits.conf \  
&& echo '' >> /etc/security/limits.conf  
  
# install zookeeper  
run mkdir -p /tmp/pge/zookeeper \  
&& wget --quiet --output-document /tmp/pge/zookeeper/zookeeper-3.4.9.tar.gz \  
http://apache.mirrors.lucidnetworks.net/zookeeper/zookeeper-3.4.9/zookeeper-3.4.9.tar.gz
\  
&& tar -C /opt -xzf /tmp/pge/zookeeper/zookeeper-3.4.9.tar.gz \  
&& ln -s /opt/zookeeper-3.4.9 /opt/zookeeper \  
&& chown -R root:root /opt/zookeeper-3.4.9/ \  
&& rm -f /opt/zookeeper/bin/*.cmd \  
&& mkdir -p /var/zookeeper  
env ZOOKEEPER_HOME /opt/zookeeper  
env PATH $PATH:$ZOOKEEPER_HOME/bin  
add zookeeper/zoo.cfg $ZOOKEEPER_HOME/conf  
run echo '' >> /etc/environment \  
&& echo 'export ZOOKEEPER_HOME=/opt/zookeeper' >> /etc/environment \  
&& echo '' >> /etc/environment \  
&& echo '' >> /root/.bashrc \  
&& echo 'export ZOOKEEPER_HOME=/opt/zookeeper' >> /root/.bashrc \  
&& echo '' >> /root/.bashrc  
  
# install accumulo  
run mkdir -p /tmp/pge/accumulo \  
&& wget --quiet --output-document /tmp/pge/accumulo/accumulo-1.6.6-bin.tar.gz
\  
http://archive.apache.org/dist/accumulo/1.6.6/accumulo-1.6.6-bin.tar.gz \  
&& tar -C /opt -xzf /tmp/pge/accumulo/accumulo-1.6.6-bin.tar.gz \  
&& chown -R root:root /opt/accumulo-1.6.6 \  
&& ln -s /opt/accumulo-1.6.6 /opt/accumulo \  
&& rm -f /opt/accumulo/bin/*.cmd  
env ACCUMULO_HOME /opt/accumulo  
env PATH $PATH:$ACCUMULO_HOME/bin  
add accumulo/1GB/standalone/* $ACCUMULO_HOME/conf/  
run rm -f $ACCUMULO_HOME/conf/accumulo-env.sh \  
&& rm -f $ACCUMULO_HOME/conf/accumulo-site.xml  
add accumulo/accumulo-env.sh $ACCUMULO_HOME/conf  
add accumulo/accumulo-site.xml $ACCUMULO_HOME/conf  
run echo '' >> /etc/environment \  
&& echo 'export ACCUMULO_HOME=/opt/accumulo' >> /etc/environment \  
&& echo 'export PATH=$ACCUMULO_HOME/bin:$PATH' >> /etc/environment \  
&& echo '' >> /etc/environment \  
&& echo '' >> /root/.bashrc \  
&& echo 'export ACCUMULO_HOME=/opt/accumulo' >> /root/.bashrc \  
&& echo 'export PATH=$ACCUMULO_HOME/bin:$PATH' >> /root/.bashrc \  
&& echo '' >> /root/.bashrc  
  
add init_accumulo.sh /etc/init_accumulo.sh  
run chown root:root /etc/init_accumulo.sh \  
&& chmod 700 /etc/init_accumulo.sh  
  
run rm -f /etc/bootstrap.sh  
add bootstrap.sh /etc/bootstrap.sh  
run chown root:root /etc/bootstrap.sh \  
&& chmod 700 /etc/bootstrap.sh  
  
expose 2181 9000 50095  
  
  

