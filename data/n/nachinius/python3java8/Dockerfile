  
FROM buildpack-deps:trusty  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# remove several traces of debian python  
RUN apt-get purge -y python.*  
  
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
ENV PYTHON_PIP_VERSION 7.1.0  
RUN set -x \  
&& mkdir -p /usr/src/python \  
&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& gpg --verify python.tar.xz.asc \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz* \  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& pip3 install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s easy_install-3.4 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python-config3 python-config  
  
CMD ["python3"]  

