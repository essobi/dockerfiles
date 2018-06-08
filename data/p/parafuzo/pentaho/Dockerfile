FROM java:7  
MAINTAINER Dev Team dev@parafuzo.com  
  
ENV PENTAHO_VERSION=5.4  
ENV PENTAHO_TAG=5.4.0.1-130  
ENV PENTAHO_HOME=/opt/pentaho  
RUN . /etc/environment  
ENV PENTAHO_JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >>
/etc/apt/sources.list  
RUN echo "deb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt
all main" >> /etc/apt/sources.list  
  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29 && \  
apt-get update && \  
apt-get install -y --force-yes git x11vnc xvfb firefox-mozilla-build python2.7
cron && \  
apt-get remove -y iceweasel && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
RUN wget
https://pypi.python.org/packages/source/s/setuptools/setuptools-20.2.2.tar.gz
&& \  
tar xvfz setuptools-20.2.2.tar.gz && \  
cd setuptools-20.2.2 && python setup.py install  
  
RUN wget https://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz && \  
tar xvfz pip-1.2.1.tar.gz && \  
cd pip-1.2.1 && python setup.py install && \  
pip install selenium retrying  
  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.10.0/geckodriver-v0.10.0-linux64.tar.gz
&& \  
tar xvfz geckodriver-v0.10.0-linux64.tar.gz && \  
mv geckodriver /usr/bin/ && chmod +x /usr/bin/geckodriver  
  
RUN rm -rf /tmp/* /var/tmp/*  
  
RUN echo "America/Sao_Paulo" > /etc/timezone; dpkg-reconfigure -f
noninteractive tzdata  
  
CMD ['/bin/bash']  

