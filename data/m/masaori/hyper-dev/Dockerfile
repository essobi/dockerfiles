FROM buildpack-deps:jessie  
  
WORKDIR /opt/hyper  
  
RUN apt-get purge -y python.*  
  
ENV OPENSSL_VERSION 1.0.2d  
ENV OPENSSL_GPG_PUBLIC_KEY_ID 0E604491  
  
ENV PYTHON_VERSION 2.7.10  
ENV PYTHON_GPG_PUBLIC_KEY_ID C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
ENV PYTHON_PIP_VERSION 7.1.0  
# Download openssl  
RUN wget "https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz" &&
\  
wget "https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz.asc" &&
\  
gpg --keyserver ha.pool.sks-keyservers.net --recv-key
${OPENSSL_GPG_PUBLIC_KEY_ID} && \  
gpg --verify openssl-${OPENSSL_VERSION}.tar.gz.asc  
  
# Download python  
RUN wget
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz"
&& \  
wget
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc"
&& \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
${PYTHON_GPG_PUBLIC_KEY_ID} && \  
gpg --verify Python-${PYTHON_VERSION}.tar.xz.asc  
  
# Build openssl  
RUN tar xvf openssl-${OPENSSL_VERSION}.tar.gz -C /usr/local/src/ && \  
cd /usr/local/src/openssl-${OPENSSL_VERSION} && \  
./config shared zlib && \  
make -j$(nproc) && \  
make test && \  
make install  
  
RUN echo "/usr/local/ssl/lib" > /etc/ld.so.conf.d/openssl.conf && \  
ldconfig  
  
ENV PKG_CONFIG_PATH $PKG_CONFIG_PATH:/usr/local/ssl/lib/pkgconfig  
ENV PATH $PATH:/usr/local/ssl/bin  
  
# Build python  
RUN tar xvf Python-${PYTHON_VERSION}.tar.xz -C /usr/local/src/ && \  
cd /usr/local/src/Python-${PYTHON_VERSION} && \  
./configure --enable-shared && \  
make -j$(nproc) && \  
make install  
  
RUN ldconfig  
  
# Install pip and packages  
RUN curl -k -SL 'https://bootstrap.pypa.io/get-pip.py' | /usr/local/bin/python
&& \  
pip install --no-cache-dir --upgrade pip==${PYTHON_PIP_VERSION}  
  
RUN pip install --no-cache-dir \  
virtualenv \  
tox \  
ipython  
  
RUN pip install cryptography --no-cache-dir \  
\--global-option=build_ext --global-option="-L/usr/local/ssl/lib" \  
\--global-option=build_ext --global-option="-I/usr/local/ssl/include"  
  
RUN wget
https://raw.githubusercontent.com/Lukasa/hyper/development/test_requirements.txt
&& \  
pip install -r test_requirements.txt  

