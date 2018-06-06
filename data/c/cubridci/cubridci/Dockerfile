FROM centos:6  
LABEL Description="This is a build and test environment image for CUBRID"  
  
RUN set -x \  
&& yum install -y centos-release-scl \  
&& yum install -y --setopt=tsflags=nodocs devtoolset-6-gcc
devtoolset-6-gcc-c++ devtoolset-6-make \  
devtoolset-6-elfutils-libelf-devel devtoolset-6-systemtap-sdt-devel \  
ncurses-devel cmake java-1.8.0-openjdk-devel ant bison flex git19 wget libxslt
\  
rpm-build libtool libtool-ltdl autoconf automake \  
&& yum clean all -y  
  
ENV WORKDIR /home  
ENV JAVA_HOME /usr/lib/jvm/java  
  
# CUBRID envronment variables  
ENV CUBRID $WORKDIR/CUBRID  
ENV CUBRID_DATABASES $CUBRID/databases  
ENV PATH $CUBRID/bin:/opt/rh/git19/root/usr/bin:$PATH  
ENV LD_LIBRARY_PATH $CUBRID/lib  
ENV TEST_SUITE medium:sql  
ENV TEST_REPORT /tmp/tests  
ENV BRANCH_TESTTOOLS master  
ENV BRANCH_TESTCASES develop  
  
# set timezone for test  
ENV TZ Asia/Seoul  
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
RUN echo 'ZONE="Asia/Seoul' > /etc/sysconfig/clock  
  
RUN chmod 777 $WORKDIR  
  
WORKDIR $WORKDIR  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["scl", "enable", "devtoolset-6", "--", "/entrypoint.sh"]  

