FROM centos:7  
  
RUN yum update -y && \  
yum install -y make wget gcc e2fsprogs openssl && \  
yum clean all  
  
RUN mkdir -p /opt \  
&& cd /opt \  
&& curl -O http://www.unixodbc.org/pub/unixODBC/unixODBC-2.3.1.tar.gz \  
&& tar xvzf unixODBC-2.3.1.tar.gz \  
&& cd unixODBC-2.3.1 \  
&& export CPPFLAGS="-DSIZEOF_LONG_INT=8" \  
&& ./configure --prefix=/usr --libdir=/usr/lib64 --sysconfdir=/etc --enable-
gui=no \--enable-drivers=no \--enable-iconv \--with-iconv-char-enc=UTF8
--with-iconv-ucode-enc=UTF16LE \  
&& make && make install  
  
RUN curl -O
https://download.microsoft.com/download/B/C/D/BCDD264C-7517-4B7D-8159-C99FC5535680/msodbcsql-13.0.0.0.tar.gz
\  
&& tar xvzf msodbcsql-13.0.0.0.tar.gz \  
&& cd msodbcsql-13.0.0.0 \  
&& ./install.sh install --accept-license  
  
ENTRYPOINT ["/usr/bin/sqlcmd"]

