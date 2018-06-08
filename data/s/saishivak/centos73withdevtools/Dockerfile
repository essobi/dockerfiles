FROM centos:7.3.1611  
MAINTAINER Saishiva K <Saishiva_K@Dell.com>  
  
RUN yum -y update; yum clean all  
RUN yum -y install openssh-server passwd wget net-tools gcc subversion
mod_dav_svn; yum clean all  
ADD ./start.sh /start.sh  
RUN mkdir /var/run/sshd  
  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
  
RUN chmod 755 /start.sh  
# EXPOSE 22  
RUN ./start.sh  
RUN wget
https://pypi.python.org/packages/source/s/setuptools/setuptools-7.0.tar.gz
--no-check-certificate  
RUN tar xzf setuptools-7.0.tar.gz  
RUN python setuptools-7.0/setup.py install  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install enum  
RUN ln /usr/lib64/libpython2.7.so.1.0 /usr/lib64/libpython2.7.so  
RUN pip install pysnmp  
RUN mkdir /omsdksvn && svnadmin create /omsdksvn && svnserve -d -r /omsdksvn  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]  

