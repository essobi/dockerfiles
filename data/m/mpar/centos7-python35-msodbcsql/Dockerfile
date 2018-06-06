FROM centos:centos7  
ADD https://packages.microsoft.com/config/rhel/7/prod.repo
/etc/yum.repos.d/mssql-release.repo  
RUN yum -y update && \  
yum -y install epel-release && \  
yum group install -y "development tools" && \  
yum install -y zlib-devel bzip2-devel openssl-devel sqlite-devel && \  
yum -y remove unixODBC-utf16 unixODBC-utf16-devel && \  
ACCEPT_EULA=Y yum -y install msodbcsql mssql-tools unixODBC-devel && \  
yum install -y gcc-c++ && \  
yum clean all  
  
# Install Python 3.5  
RUN curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz && \  
tar xf Python-3.5.0.tgz && \  
cd Python-3.5.0 && \  
./configure --prefix=/usr/local \--enable-shared LDFLAGS="-Wl,-rpath
/usr/local/lib" && \  
make && make altinstall && \  
cd .. && rm -f Python-3.5.0.tgz && rm -rf Python-3.5.0 && \  
curl https://bootstrap.pypa.io/get-pip.py | python3.5  
  
RUN pip install pyodbc  

