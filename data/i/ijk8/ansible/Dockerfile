FROM centos:7  
RUN yum update -y  
RUN yum install -y \  
git \  
gcc \  
make \  
tcl \  
openssl-devel \  
python-setuptools \  
python-devel && \  
easy_install pip && \  
pip install \  
six \  
httplib2  
RUN pip install ansible==2.0.1.0  
RUN curl "https://www.fossil-scm.org/index.html/tarball/fossil-src.tar.gz" |
tar zx  
RUN cd fossil-src && \  
./configure --disable-fusefs \  
\--json --with-th1-docs --with-th1-hooks \  
\--with-tcl --with-tcl-stubs --with-tcl-private-stubs && \  
make && strip fossil && make install && \  
cd .. && rm -rf fossil-src  
  
EXPOSE 80  
CMD ["fossil", "server", "--create", "--user", "admin", "/root/repo.fossil", "
--port", "80", "--nojail"]  

