# Python 2.7 on CentOS 7  
#  
# --- Image Stack ---  
# luzh/python2.7-baseline  
# luzh/centos7  
FROM luzh/centos7  
  
# Set the Python version to be built and installed.  
ENV PYTHON_VERSION 2.7.11  
# https://github.com/docker-library/python/blob/master/2.7/Dockerfile  
# If this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'".  
ENV PYTHON_PIP_VERSION 8.1.1  
# Enable UTF-32 in Python 2.7 by flag "--enable-unicode=ucs4". In Python 3.2
the flag is "--with-wide-unicode".  
# Compile Python as a shared library: --enable-shared LDFLAGS="-Wl,-rpath
/usr/local/lib"  
# The installation prefix is "/usr/local", and the system's Python will still
exist in "/usr".  
# CRITICAL: Use "make altinstall" instead of "make install" on CentOS 7, in
order not to override system defaults.  
# CentOS depends on a specific Python version in "/usr/bin" to operate,
especially yum.  
# Therefore it is required to install newer Python versions in alternative
directories such as "/usr/local".  
  
RUN mkdir /build && cd /build \  
&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz"
-o python.tgz \  
&& mkdir /build/python \  
&& yum -y install wget tar zip unzip make gcc gcc-c++ \  
&& yum -y install zlib zlib-devel \  
&& yum -y install bzip2 bzip2-devel \  
&& yum -y install openssl openssl-devel \  
&& yum -y install ncurses ncurses-devel \  
&& yum -y install sqlite sqlite-devel \  
&& yum -y install readline readline-devel \  
&& yum -y install tk tk-devel \  
&& yum -y install gdbm gdbm-devel \  
&& yum -y install libdb libdb-devel \  
&& yum -y install db4 db4-devel \  
&& yum -y install libpcap libpcap-devel \  
&& yum -y install xz xz-devel \  
&& tar -zxvf python.tgz --strip-components=1 -C /build/python \  
&& cd /build/python \  
&& ./configure --prefix=/usr/local --enable-shared --enable-unicode=ucs4
LDFLAGS="-Wl,-rpath /usr/local/lib" \  
&& make -j$(nproc) \  
&& make altinstall \  
&& if [ "$(/usr/local/bin/python2.7 -V 2>&1)" == "Python $PYTHON_VERSION" ]; \  
then \  
echo; echo -e "\e[32mDone: Python $PYTHON_VERSION is installed
successfully.\e[0m"; echo; \  
else \  
echo; echo -e "\e[31mError: Python $PYTHON_VERSION is probably NOT correctly
installed.\e[0m"; echo; \  
fi \  
&& curl -SL 'https://bootstrap.pypa.io/get-pip.py' | /usr/local/bin/python2.7
\  
&& pip install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-or \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-delete \  
&& cd && rm -rf /build \  
&& yum clean all  
  
# Not all Python modules are built in this installation. When the Python build  
# is finished, the following modules may not be found (not built with Python):  
# bsddb185 dl imageop sunaudiodev  
#  
# These are not necessary for this CentOS build.  
# bsddb185: Interface to Oracle Berkeley DB, deprecated.  
# dl: For 32-bit machines, deprecated since Python 2.6. Use ctypes instead.  
# imageop: For 32-bit machines, deprecated since Python 2.6. Use PIL/Pillow
instead.  
# sunaudiodev: For Sun hardware, deprecated since Python 2.6. It's not needed
for a CentOS build.  
# Entrypoint Executable  
# To override the entrypoint, run docker with "--entrypoint=bash".  
ENTRYPOINT ["/usr/local/bin/python2.7"]  
  
# Entrypoint Options  
# Simply show the installed Python version if CMD is not overwritten at run
time.  
CMD ["-V"]  

