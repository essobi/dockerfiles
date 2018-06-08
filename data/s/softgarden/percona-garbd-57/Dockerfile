FROM centos:7  
MAINTAINER Stefan Schueffler <s.schueffler@softgarden.de>  
  
RUN set -x \  
&& yum -y update \  
&& rpmkeys \--import https://www.percona.com/downloads/RPM-GPG-KEY-percona \  
&& yum -y install http://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm \  
&& yum -y install Percona-XtraDB-Cluster-garbd-57 \  
&& yum clean all  
  
EXPOSE 3306 4444 4567 4567/udp 4568  
  
ENTRYPOINT ["/usr/bin/garbd"]  

