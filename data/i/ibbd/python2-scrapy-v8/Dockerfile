#  
# python2-scrapy-v8 Dockerfile  
# 在python2-scrapy镜像的基础上增加v8解释引擎及pyv8  
#  
# https://github.com/ibbd/dockerfile-python/scrapy/v8  
#  
# sudo docker build -t ibbd/python2-scrapy-v8 ./  
#  
# Pull base image.  
FROM ibbd/python2-scrapy  
  
MAINTAINER Alex Cai "cyy0523xc@gmail.com"  
# 安装依赖  
#RUN \  
#apt-get update \  
#&& apt-get install -y --no-install-recommends \  
#curl \  
#&& rm -rf /var/lib/apt/lists/*  
# 安装V8  
# install pyv8  
# libboost-all-dev \  
# @see http://www.cnblogs.com/vingi/articles/4131633.html  
RUN \  
set -x \  
&& buildDeps=' \  
subversion \  
build-essential \  
libreadline-dev \  
scons \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
curl \  
python-dev \  
libboost-dev \  
libboost-thread-dev \  
libboost-system-dev \  
libboost-python-dev \  
&& cd /root/ \  
&& svn checkout http://v8.googlecode.com/svn/trunk/ v8 \  
&& svn checkout http://pyv8.googlecode.com/svn/trunk/ pyv8 \  
&& cd v8 \  
&& export V8_HOME=`/root/v8` \  
&& cd ../pyv8 \  
&& python setup.py build \  
&& python setup.py install \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& rm -rf /var/lib/apt/lists/*  
  

