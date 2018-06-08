FROM lonefreak/fpm  
MAINTAINER Fabricio Leotti <fabricio.leotti@gmail.com>  
  
ENV PYTHON_VERSION 2.7.8  
ENV PYTHON_INSTALL_DIR /opt  
  
RUN yum groupinstall -y "Development tools" \  
&& yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-
devel \  
&& yum clean all  
RUN wget --no-check-certificate -P $PYTHON_INSTALL_DIR
https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz
\  
&& tar xf $PYTHON_INSTALL_DIR/Python-$PYTHON_VERSION.tar.xz -C
$PYTHON_INSTALL_DIR \  
&& cd $PYTHON_INSTALL_DIR/Python-$PYTHON_VERSION \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make altinstall  
RUN ln -s /usr/local/bin/python2.7 /usr/local/bin/python27  
RUN cd /tmp \  
&& wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py \  
&& python27 ez_setup.py \  
&& /usr/local/bin/easy_install-2.7 pip  
RUN pip install -U pip \  
&& pip install virtualenv  
  
ADD build.sh /build.sh  
ENTRYPOINT []  
CMD []

