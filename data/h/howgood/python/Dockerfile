# HowGood Python Container  
# howgood/python  
  
FROM howgood/base  
  
################################################  
# Copied from python:2.7 https://goo.gl/mz3Aww #  
################################################  
  
ENV PATH /usr/local/bin:$PATH  
  
ENV LANG C.UTF-8  
  
# runtime dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
tcl \  
tk \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
ENV PYTHON_VERSION 2.7.13  
ENV PYTHON_PIP_VERSION 9.0.1  
  
RUN set -ex \  
&& buildDeps=' \  
tcl-dev \  
tk-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& ./configure \  
\--enable-shared \  
\--enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
\  
&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& python2 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \  
&& rm /tmp/get-pip.py \  
# we use "--force-reinstall" for the case where the version of pip we're
trying to install is the same as the version bundled with Python  
# ("Requirement already up-to-date: pip==8.1.2 in
/usr/local/lib/python3.6/site-packages")  
# https://github.com/docker-library/python/pull/143#issuecomment-241032683  
&& pip install --no-cache-dir --upgrade --force-reinstall
"pip==$PYTHON_PIP_VERSION" \  
# then we use "pip list" to ensure we don't have more than one pip version
installed  
# https://github.com/docker-library/python/pull/100  
&& [ "$(pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" { print $2; exit }')"
= "$PYTHON_PIP_VERSION" ] \  
\  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' + \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /usr/src/python ~/.cache /tmp/*  
  
############  
# End copy #  
############  
  
# Python env  
ENV PYTHONDONTWRITEBYTECODE=1 \  
PYTHONUNBUFFERED=1 \  
C_FORCE_ROOT=1 \  
XDG_CACHE_HOME=/tmp  

