FROM debian:jessie  
  
COPY ./mha4mysql-manager.tar.gz /tmp/  
COPY ./mha4mysql-node.tar.gz /tmp/  
  
RUN build_deps='ssh sshpass perl libdbi-perl libmodule-install-perl libdbd-
mysql-perl libconfig-tiny-perl liblog-dispatch-perl libparallel-forkmanager-
perl make' \  
&& apt-get update \  
&& apt-get -y \--force-yes install $build_deps \  
&& tar -zxf /tmp/mha4mysql-node.tar.gz -C /opt \  
&& cd /opt/mha4mysql-node \  
&& perl Makefile.PL \  
&& make \  
&& make install \  
&& tar -zxf /tmp/mha4mysql-manager.tar.gz -C /opt \  
&& cd /opt/mha4mysql-manager \  
&& perl Makefile.PL \  
&& make \  
&& make install \  
&& cd /opt \  
&& rm -rf /opt/mha4mysql-* \  
&& apt-get clean

