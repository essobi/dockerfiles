FROM centos:7  
MAINTAINER devops@leonisand.co  
  
RUN yum -y update \  
&& yum -y install make \  
&& yum -y install wget perl-TermReadKey perl-DBI perl-DBD-mysql perl-ExtUtils-
MakeMaker perl-Time-HiRes \  
&& yum clean all  
  
WORKDIR /var  
  
RUN wget https://github.com/innotop/innotop/archive/v1.11.1.tar.gz \  
&& tar xvzf v1.11.1.tar.gz \  
&& cd ./innotop-1.11.1 \  
&& perl Makefile.PL \  
&& make install \  
&& cd ../ \  
&& rm -rf ./innotop-1.11.1 ./v1.11.1.tar.gz  
  
ENTRYPOINT ["/usr/local/bin/innotop"]  
  

