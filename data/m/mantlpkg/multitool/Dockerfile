FROM centos:7  
MAINTAINER Brian Hicks <brian@aster.is>  
  
# development tools  
RUN yum groupinstall -y "Development Tools"  
  
# FPM  
RUN yum install -y ruby ruby-devel  
RUN gem install fpm --no-rdoc --no-ri  
  
# peer packages  
COPY mantl-rpm.repo /etc/yum.repos.d/  
  
# hammer  
ADD https://github.com/asteris-
llc/hammer/releases/download/1.0.0/hammer_1.0.0_linux_amd64.tar.gz
/tmp/hammer.tgz  
RUN cd /tmp && \  
tar -xzvf /tmp/hammer.tgz && \  
cp /tmp/hammer_1.0.0_linux_amd64/hammer /usr/bin/hammer && \  
rm -rf /tmp/hammer*  
  
# scripts  
COPY entry.sh /bin/entry  
ENTRYPOINT ["/bin/entry"]  

