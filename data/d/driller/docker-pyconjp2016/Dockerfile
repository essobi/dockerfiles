FROM alpine:latest  
  
RUN apk update \  
&& apk add \  
ca-certificates \  
libstdc++ \  
libgfortran \  
freetype \  
python3 \  
&& apk add --virtual=build_dependencies \  
cmake \  
gcc \  
g++ \  
make \  
musl-dev \  
linux-headers \  
freetype-dev \  
libpng \  
git \  
bash \  
openssh \  
gfortran \  
python3-dev \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& python3 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& python3 -m pip --no-cache-dir install pip -U \  
&& mkdir -p /tmp/build \  
&& cd /tmp/build/ \  
&& wget http://www.netlib.org/blas/blas-3.6.0.tgz \  
&& wget http://www.netlib.org/lapack/lapack-3.6.1.tgz \  
&& tar xzf blas-3.6.0.tgz \  
&& tar xzf lapack-3.6.1.tgz \  
&& cd /tmp/build/BLAS-3.6.0/ \  
&& gfortran -O3 -std=legacy -m64 -fno-second-underscore -fPIC -c *.f \  
&& ar r libfblas.a *.o \  
&& ranlib libfblas.a \  
&& mv libfblas.a /tmp/build/. \  
&& cd /tmp/build/lapack-3.6.1/ \  
&& sed -e "s/frecursive/fPIC/g" -e "s/ \.\.\// /g" -e
"s/^CBLASLIB/\#CBLASLIB/g" make.inc.example > make.inc \  
&& make lapacklib \  
&& make clean \  
&& mv liblapack.a /tmp/build/. \  
&& export BLAS=/tmp/build/libfblas.a \  
&& export LAPACK=/tmp/build/liblapack.a \  
&& cd /tmp/build/ \  
&& git clone -b issue37-Python3 https://github.com/JrtPec/python-
highcharts.git \  
&& cd python-highcharts \  
&& python3 setup.py install \  
&& cd / \  
&& python3 -m pip --no-cache-dir install \  
seaborn \  
jupyter \  
pandas \  
pandas_datareader \  
xlrd \  
requests \  
pyyaml \  
&& python3 -m pip --no-cache-dir install \  
https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
\  
&& jupyter contrib nbextension install \  
&& jupyter nbextensions_configurator enable \  
&& jupyter nbextension enable --py --sys-prefix widgetsnbextension \  
&& apk del --purge -r build_dependencies \  
&& rm -rf /tmp/build \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /notebooks  
  
VOLUME /notebooks  
ENTRYPOINT /usr/bin/jupyter-notebook --no-browser --ip=0.0.0.0 --notebook-
dir=/notebooks  
EXPOSE 8888  

