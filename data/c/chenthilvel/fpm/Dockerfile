FROM centos:6  
MAINTAINER ChenthilVel  
RUN yum -y update && yum -y install rpm-build && yum clean all  
RUN curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -  
RUN curl -L get.rvm.io | bash -s stable  
RUN source /etc/profile.d/rvm.sh && /usr/local/rvm/bin/rvm requirements &&
/usr/local/rvm/bin/rvm install 2.3.0 && /usr/local/rvm/bin/rvm cleanup all  
RUN bash -lc "rvm use --default 2.3.0 && rvm rubygems current && gem install
fpm && rvm cleanup all && gem cleanup"  
CMD ["/bin/bash"]  

