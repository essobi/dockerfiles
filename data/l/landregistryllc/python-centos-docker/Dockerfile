FROM centos:7  
  
RUN yum upgrade -y && \  
yum groupinstall -y "Development Tools" && \  
yum install -y postgresql-devel zlib-devel readline-devel bzip2-devel openssl-
devel && \  
yum clean all  
  
ENV LANG C.UTF-8  
ENV GPG_KEY 97FC712E4C024BBEA48A61ED3A5CA953F73C700D  
ENV PYTHON_VERSION 3.5.1  
ENV PYTHON_PIP_VERSION 8.1.2  
  
RUN set -ex \  
&& echo "export PATH=\$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh \  
&& echo "/usr/local/lib" > /etc/ld.so.conf.d/local_lib.conf \  
&& export PATH=$PATH:/usr/local/bin \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://hkps.pool.sks-keyservers.net:80 \--recv-keys
"$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python \--strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& pip3 install --no-cache-dir --upgrade --ignore-installed
pip==$PYTHON_PIP_VERSION \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \   
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python ~/.cache  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s easy_install-3.5 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
CMD ["python3"]  
  
  
  

