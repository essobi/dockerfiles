FROM oscarraig/c7-systemd  
RUN yum -y groupinstall "Development Tools"  
RUN yum -y install vim  
RUN yum -y install wget  
RUN yum -y install boost-program-options.x86_64  
RUN yum -y install boost-devel-1.53.0-23.el7.x86_64  
RUN yum -y install valgrind.x86_64  
RUN wget http://sourceforge.net/projects/log4cplus/files/log4cplus-
stable/1.1.3/log4cplus-1.1.3-rc5.tar.gz  
RUN tar zxfv log4cplus-1.1.3-rc5.tar.gz  
RUN rm log4cplus-1.1.3-rc5.tar.gz  
RUN ./log4cplus-1.1.3-rc5/configure && make && make install  
RUN wget https://googletest.googlecode.com/files/gtest-1.7.0.zip  
RUN unzip gtest-1.7.0.zip  
RUN rm gtest-1.7.0.zip  
RUN cd gtest-1.7.0 && ./configure && make && cp -R include/ /usr/local/ && cp
./lib/.libs/* /usr/local/lib/  
RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum -y update  
RUN yum -y install python-pip  
RUN pip install cpp-coveralls  
CMD /bin/bash  
  

