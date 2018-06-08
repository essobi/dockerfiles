  
FROM qenn/centos6-ruby  
MAINTAINER Qen Empaces <qen.empaces@gmail.com>  
  
ENV HOME /root  
ENV SHELL /bin/bash  
  
RUN ln -s /bin/sh /usr/sh  
RUN touch /usr/local/src/rubinius-2.4.1.tar.bz2  
RUN git clone git://github.com/rubinius/rubinius.git
/usr/local/src/rubinius-2.4.1 && cd /usr/local/src/rubinius-2.4.1 && git
checkout 010342ac4da91a6c671bebe4b6206022761f0071  
RUN SHELL='/bin/bash' LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 ruby-install
--cleanup --no-download --no-extract --system rbx 2.4.1  
RUN echo 'export PATH=/usr/local/rubinius/2.4/bin:$PATH' >> /etc/bashrc  
  
# clean up  
RUN rm -rf /usr/local/src/*  
RUN yum clean all && rm -rf /var/cache/yum/*  
RUN rm -rf /ruby-install-*  
  

