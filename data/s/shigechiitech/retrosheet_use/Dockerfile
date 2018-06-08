FROM centos:latest  
  
# wget/gcc/make/git/httpd/mysql install  
RUN yum -y install wget gcc make git httpd mysql  
  
# chadwick  
RUN mkdir -p /retrosheet/chadwick && \  
cd /retrosheet/chadwick && \  
wget
http://sourceforge.net/projects/chadwick/files/chadwick-0.6/chadwick-0.6.5/chadwick-0.6.5.tar.gz
&& \  
tar zxvf chadwick-0.6.5.tar.gz && \  
pwd && \  
ls -la && \  
cd /retrosheet/chadwick/chadwick-0.6.5 && \  
./configure && \  
make && \  
make install && \  
ln -s /usr/local/lib/libchadwick.so.0 /usr/lib/libchadwick.so.0  
  
# py-retrosheet(only Python2)  
RUN yum -y install epel-release && \  
yum -y install python2-pip && \  
pip install pip --upgrade && \  
pip install sqlalchemy && \  
pip install PyMySQL  
RUN cd /retrosheet && \  
git clone https://github.com/wellsoliver/py-retrosheet.git  
  
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]  

