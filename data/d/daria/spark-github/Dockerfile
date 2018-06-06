FROM buildpack-deps:wheezy  
  
#====Codenvy to Move Python Files from Codenvy server to Remote Server====  
EXPOSE 8080  
ENV CODENVY_APP_PORT_8080_HTTP 8080  
ENV CODENVY_WEB_SHELL_PORT 4200  
RUN mkdir /tmp/application  
RUN mkdir /application  
  
ENV CODENVY_APP_BIND_DIR /application  
  
VOLUME ["/application"]  
  
# ADD $app$/requirements.txt /tmp/application/requirements.txt  
# ADD $app$/main.py /application/main.py  
#===========================Start Update
Debian================================  
RUN apt-get -y update > /dev/null 2>&1  
RUN apt-get -y upgrade > /dev/null 2>&1  
RUN apt-get -y install apt-utils > /dev/null 2>&1  
RUN apt-get -y update > /dev/null 2>&1  
RUN apt-get -y upgrade > /dev/null 2>&1  
RUN apt-get -y install build-essential > /dev/null 2>&1  
#===========================End Update
Debian==================================  
#===========================Start Install Python and
PIP=======================  
# remove several traces of debian python  
RUN apt-get purge -y python.* > /dev/null 2>&1  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# gpg: key F73C700D: public key "Larry Hastings <larry@hastings.org>" imported  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
97FC712E4C024BBEA48A61ED3A5CA953F73C700D  
  
ENV PYTHON_VERSION 3.4.3  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 7.0.1  
# work done here  
#RUN set -x > /dev/null 2>&1 \  
#&& mkdir -p /usr/src/python > /dev/null 2>&1 \  
#&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz > /dev/null 2>&1 \  
#&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc > /dev/null 2>&1 \  
#&& gpg --verify python.tar.xz.asc > /dev/null 2>&1 \  
#&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz > /dev/null
2>&1 \  
#&& rm python.tar.xz* > /dev/null 2>&1 \  
#&& cd /usr/src/python > /dev/null 2>&1 \  
#&& ./configure --enable-shared --enable-unicode=ucs4 > /dev/null 2>&1 \  
#&& make -j$(nproc) > /dev/null 2>&1 \  
#&& make install > /dev/null 2>&1 \  
#&& ldconfig > /dev/null 2>&1 \  
#&& pip3 install --upgrade pip==$PYTHON_PIP_VERSION > /dev/null 2>&1 \  
#&& find /usr/local \  
#\\( -type d -a -name test -o -name tests \\) \  
#-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
#-exec rm -rf '{}' + > /dev/null 2>&1 \  
#&& rm -rf /usr/src/python > /dev/null 2>&1  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin > /dev/null 2>&1 \  
&& ln -s easy_install-3.4 easy_install > /dev/null 2>&1 \  
&& ln -s idle3 idle > /dev/null 2>&1 \  
&& ln -s pydoc3 pydoc > /dev/null 2>&1 \  
&& ln -s python3 python > /dev/null 2>&1 \  
&& ln -s python-config3 python-config > /dev/null 2>&1  
#===========================End Install Python and
PIP=========================  
#===========================Start Install
Spark================================  
RUN apt-get install -y openjdk-7-jdk  
RUN wget
http://downloads.typesafe.com/scala/2.11.7/scala-2.11.7.tgz?_ga=1.249840389.2063384723.1435684037  
RUN mkdir /usr/local/src/scala  
RUN tar -xvzf scala-2.11.7.tgz?_ga=1.249840389.2063384723.1435684037 -C
/usr/local/src/scala/  
RUN export SCALA_HOME=/usr/local/src/scala/scala-2.11.7  
RUN export PATH=$SCALA_HOME/bin:$PATH  
RUN apt-get install -y git  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.4.0.tgz  
RUN mkdir /spark  
RUN tar -xvzf spark-1.4.0.tgz -C /spark  
#===========================End Install
Spark==================================  
#===========================Start Install
virtualenv===========================  
#RUN pip3 install virtualenv  
#===========================End Install
virtualenv=============================  
#===========================Start Install Python
Requirements==================  
#RUN cd /tmp/application && \  
# virtualenv /env && \  
#/env/bin/pip3 install -r requirements.txt  
#===========================End Install Python
Requirements====================  
#===========================Start
Program======================================  
# 1. Update permissions recursively  
# 2. Make newly created files accessible for anyone  
# 3. Start application  
#RUN chmod a+rw -R /application/ && \  
# umask 0 &&  
# /env/bin/python3 /application/$executable:-main.py$  
#===========================Start
Program======================================  
#===========================Start
shellinabox==================================  
RUN apt-get update && \  
apt-get -y install sudo procps wget unzip gcc make  
RUN mkdir /opt/shellinabox && \  
wget -qO- "https://shellinabox.googlecode.com/files/shellinabox-2.14.tar.gz" |
tar -zx --strip-components=1 -C /opt/shellinabox  
RUN cd /opt/shellinabox > /dev/null 2>&1 && \  
./configure > /dev/null 2>&1 && \  
make > /dev/null 2>&1  
USER root  
EXPOSE 4200  
ENV CODENVY_WEB_SHELL_PORT 4200  
ENV service /:root:users:/home/root:/bin/bash  
#===========================End
shellinabox====================================  
#===========================Install Spark Part
2===============================  
RUN cd spark/spark-1.4.0 && build/sbt >> /dev/null 2>&1  
#===========================End Install Spark Part
2===========================  
#===========================Start
Supervisord====================================  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
#ADD $app$/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN mkdir /var/supervisord  
CMD /usr/bin/supervisord  
#===========================End
Supervisord======================================  

