FROM danielperezr88/apache2:latest  
  
MAINTAINER danielperezr88 <danielperezr88@gmail.com>  
  
RUN /usr/sbin/a2enmod alias && /usr/sbin/a2enmod proxy && /usr/sbin/a2enmod
proxy_http && /usr/sbin/a2enmod proxy_wstunnel  
  
# Install curl  
RUN apt-get update && apt-get install -y curl  
  
# Install Tini  
# In order to secure this download by checksum checking, on second line, we
could add:  
# echo "<checksum> *tini" | sha256sum -c - && \  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini >
tini && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
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
ENV PYTHON_PIP_VERSION 7.0.3  
# Install XZ-Utils  
RUN apt-get update && apt-get install -y xz-utils  
  
# Install Zlib  
RUN apt-get update && apt-get install -y zlib1g-dev  
  
# Install C/C++ Compilers  
RUN apt-get update && apt-get install -y \  
g++ \  
gcc \  
make  
  
RUN apt-get update && apt-get install -y \  
libbz2-dev \  
libssl-dev \  
libmysqlclient-dev \  
libsqlite3-dev  
  
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
&& curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python3 \  
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
  
# Install "virtualenv", since the vast majority of users of this image will
want itpip  
RUN pip install --no-cache-dir virtualenv  
  
# Install main python packages  
RUN pip install --upgrade pip && \  
pip install mysqlclient && \  
pip install regex && \  
pip install numpy && \  
pip install pandas && \  
pip install requests && \  
pip install scipy && \  
pip install scikit-learn && \  
pip install jupyter && \  
pip install Flask && \  
pip install bokeh && \  
pip install Tornado-JSON && \  
pip install -U gcloud  
  
EXPOSE 80  
ENTRYPOINT ["tini","--"]  
CMD ["/usr/local/bin/jupyter","notebook","--no-browser","--port=80","--
ip=0.0.0.0"]

