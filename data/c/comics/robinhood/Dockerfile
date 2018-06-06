FROM comics/centos  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Software: robinhood  
# Software Version: 3.1  
# Software Website: https://github.com/cea-hpc/robinhood  
# Description: Robinhood Policy Engine : a versatile tool to monitor
filesystem contents and schedule actions on filesystem entries.  
##############################################################  
  
ENV APP_NAME=robinhood  
ENV VERSION=3.1  
  
RUN yum install -y \  
https://downloads.sourceforge.net/project/robinhood/robinhood/${VERSION}/RPMS/posix_fs/robinhood-
posix-${VERSION}-1.el7.centos.x86_64.rpm \  
https://downloads.sourceforge.net/project/robinhood/robinhood/${VERSION}/RPMS/robinhood-
adm-${VERSION}-1.noarch.x86_64.rpm \  
https://downloads.sourceforge.net/project/robinhood/robinhood/${VERSION}/RPMS/robinhood-
webgui-${VERSION}-1.noarch.x86_64.rpm \  
mariadb \  
mariadb-devel ; \  
yum clean all ; \  
cp /etc/robinhood.d/templates/basic.conf /etc/robinhood.d/ ; \  
sed -i "s/\\(^\s*fs_path\\).*/\1 = \"\/work\";/" /etc/robinhood.d/basic.conf ;  
COPY robinhood_entrypoint.sh /usr/local/bin/robinhood_entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/robinhood_entrypoint.sh"]  

