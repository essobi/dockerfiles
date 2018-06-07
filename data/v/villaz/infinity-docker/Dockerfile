FROM centos:centos6  
RUN yum -y install wget  
RUN rpm --import http://emisoft.web.cern.ch/emisoft/dist/EMI/3/RPM-GPG-KEY-emi  
RUN wget http://emisoft.web.cern.ch/emisoft/dist/EMI/3/sl6/x86_64/base/emi-
release-3.0.0-2.el6.noarch.rpm  
RUN yum localinstall -y emi-release-3.0.0-2.el6.noarch.rpm  
RUN yum -y update --nogpgcheck  
RUN yum -y install
ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/mateli:/EPEL-
deps/CentOS_CentOS-6/noarch/bouncycastle-1.46-5.3.noarch.rpm  
RUN yum -y install voms-clients3 --nogpgcheck  
RUN wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y install epel-release-6-8.noarch.rpm  
RUN sed -i "s/mirrorlist=https/mirrorlist=http/" /etc/yum.repos.d/epel.repo  
RUN yum -y update --nogpgcheck  
RUN yum -y install yum-priorities  
RUN wget http://repository.egi.eu/sw/production/umd/3/sl6/x86_64/updates/umd-
release-3.0.1-1.el6.noarch.rpm  
RUN yum -y install umd-release-3.0.1-1.el6.noarch.rpm  
RUN yum -y install lcg-CA  
RUN yum -y install fetch-crl  
RUN yum -y install git  
RUN yum -y install vixie-cron  
RUN yum -y install myproxy  
  
RUN mkdir -p /etc/grid-security/vomsdir/fedcloud.egi.eu  
ADD vomses /etc/  
ADD voms1.egee.cesnet.cz.lsc /etc/grid-security/vomsdir/fedcloud.egi.eu/  
ADD voms2.grid.cesnet.cz /etc/grid-security/vomsdir/fedcloud.egi.eu/  
ADD lcg-voms2.cern.ch.lsc /etc/grid-security/vomsdir/  
ADD lcg-voms.cern.ch.lsc /etc/grid-security/vomsdir/  
ADD voms2.cern.ch.lsc /etc/grid-security/vomsdir/  
ADD voms.cern.ch.lsc /etc/grid-security/vomsdir/  
RUN mkdir -p /root/.globus  
ENV password none  
RUN echo '* */11 * * * root echo $password | voms-proxy-init -voms atlas -rfc'
> /etc/crontab  
  
#Install Node.js  
RUN curl -sL https://rpm.nodesource.com/setup | bash -  
RUN yum install -y nodejs  
RUN npm install -g typescript  
  
#Install newrelic  
RUN rpm -Uvh http://download.newrelic.com/pub/newrelic/el5/i386/newrelic-
repo-5-3.noarch.rpm  
RUN yum install -y newrelic-sysmond  
RUN mkdir -p /var/log/newrelic  
RUN chmod 777 /var/log/newrelic  
ENV relic_key none  
  
#Download and install infinity  
RUN mkdir /app  
WORKDIR /app  
RUN git clone https://bitbucket.org/Villaz/infinity.git  
WORKDIR /app/infinity  
RUN git fetch  
RUN git checkout develop  
RUN find ./src -print | grep -i ".*[.]ts" > ts-files.txt  
RUN tsc --module commonjs --target ES5 @ts-files.txt  
ADD init.sh /app/  
VOLUME /etc/infinity/conf/  
VOLUME /etc/infinity/context/  
RUN chmod 777 /app/init.sh  
  
#Add enviroment variables to use myproxy  
ENV myproxy none  
ENV password none  
  
ENTRYPOINT /app/init.sh  

