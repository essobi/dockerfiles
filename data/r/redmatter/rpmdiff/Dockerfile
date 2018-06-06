FROM centos:6  
RUN yum install -y gcc texinfo git  
  
WORKDIR /tmp  
  
RUN git clone git://github.com/lvc/pkgdiff && \  
make -C pkgdiff install  
  
ADD http://ftp.gnu.org/gnu/wdiff/wdiff-1.2.2.tar.gz /tmp  
  
RUN tar -zxvf /tmp/wdiff-1.2.2.tar.gz && \  
pushd wdiff-1.2.2 && \  
./configure && \  
make && \  
make install && \  
popd  
  
RUN yum remove -y gcc texinfo git && yum clean all && rm -rf /tmp/*  
  
WORKDIR /workspace  
ENTRYPOINT ["/usr/bin/pkgdiff"]  

