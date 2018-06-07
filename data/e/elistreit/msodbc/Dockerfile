FROM ubuntu:16.10  
LABEL name "docker-msodbc"  
LABEL version "0.0.1"  
LABEL description "Ubuntu with Python 3.6 and MS ODBC for Azure SQL Database"  
LABEL maintainer "Eli Streit — https://t.me/elistreit"  
  
ARG CONTEXT=.  
ENV CONTEXT $CONTEXT  
  
ARG WORKDIR=/usr/src/app  
ENV WORKDIR $WORKDIR  
  
ARG ODBC_TMPDIR=/tmp/msodbcubuntu  
ENV ODBC_TMPDIR $ODBC_TMPDIR  
  
ARG DEBIAN_FRONTEND=noninteractive  
ENV DEBIAN_FRONTEND $DEBIAN_FRONTEND  
  
ARG UBUNTU_VERSION=16.10  
ENV UBUNTU_VERSION $UBUNTU_VERSION  
  
ARG PYTHON_VERSION=3.6  
ENV PYTHON_VERSION $PYTHON_VERSION  
  
ARG ODBC_VERSION_UX=2.3.4  
ENV ODBC_VERSION_UX $ODBC_VERSION_UX  
  
ARG ODBC_VERSION_MS=13.1.4.0-1  
ENV ODBC_VERSION_MS $ODBC_VERSION_MS  
  
ENV PM apt -y  
ENV PMI $PM install  
ENV PMU $PM update  
ENV PYTHON python$PYTHON_VERSION  
ENV ECHO="printf \n\n\033[1;30m[Dockerfile]\t\033[1;32m%s\033[0m\n\n\n"  
RUN $ECHO "Set frontend interaction" \  
&& export DEBIAN_FRONTEND=$DEBIAN_FRONTEND  
  
RUN $ECHO "Distrib upgrading" \  
&& $PMU && $PM upgrade  
  
RUN $ECHO "Python 3.6 Installing" \  
&& $PMU && $PMI $PYTHON  
  
RUN $ECHO "PIP Installing" \  
&& $PMU && $PMI python3-pip  
  
RUN $ECHO "PIP Upgrading" \  
&& $PYTHON -m pip install --upgrade pip setuptools wheel  
  
RUN \  
$ECHO "Installing unixODBC v$ODBC_VERSION_UX" \  
&& $PMU && $PMI wget g++-6 \  
&& rm -rf $ODBC_TMPDIR && mkdir -p $ODBC_TMPDIR \  
&& wget ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-$ODBC_VERSION_UX.tar.gz
-P $ODBC_TMPDIR/ \  
&& cd $ODBC_TMPDIR \  
&& tar -xzf $ODBC_TMPDIR/unixODBC-$ODBC_VERSION_UX.tar.gz  
  
RUN \  
$ECHO "Configuring unixODBC v$ODBC_VERSION_UX" \  
&& cd $ODBC_TMPDIR/unixODBC-$ODBC_VERSION_UX/ \  
&& ./configure --disable-gui --disable-drivers \  
\--enable-iconv --with-iconv-char-enc=UTF8 \  
\--with-iconv-ucode-enc=UTF16LE 1> odbc_con.log 2> make_err.log \  
&& $ECHO "Building and Installing unixODBC v$ODBC_VERSION_UX" \  
&& make 1> make_std.log 2> make_err.log \  
&& make install 1> makeinstall_std.log 2> makeinstall_err.log \  
&& rm -rf $ODBC_TMPDIR  
  
RUN \  
$ECHO "Installing ODBC Driver for Microsoft SQL Server v$ODBC_VERSION_MS" \  
&& $PMU && $PMI curl apt-transport-https apt-utils \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -\  
&& curl https://packages.microsoft.com/config/ubuntu/$UBUNTU_VERSION/prod.list
> /etc/apt/sources.list.d/mssqlrelease.list \  
&& $PMU \  
&& ACCEPT_EULA=Y $PMI msodbcsql=$ODBC_VERSION_MS mssql-tools  
  
RUN \  
$ECHO "Installing pyODBC" \  
&& $PMU && $PMI unixodbc-dev python$PYTHON_VERSION-dev \  
&& pip install pyodbc  
  
RUN echo '#!/bin/bash\npython$PYTHON_VERSION $@' > /usr/bin/python && chmod +x
/usr/bin/python  
  
CMD ["/bin/bash"]  

