FROM ringo/scientific:7.2  
MAINTAINER Daniel Williams <daniel.williams@ligo.org>  
  
RUN yum -y groupinstall "Development Tools" "Development Libraries"; yum -y
clean all  
RUN yum install -y zlib-devel fftw-devel libxml2-devel glib2-devel; yum -y
clean all  
RUN yum install -y wget; yum -y clean all  
RUN yum install -y python-devel python-numpy; yum -y clean all  
RUN wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-9.noarch.rpm  
RUN rpm -ivh epel-release-7-9.noarch.rpm  
RUN yum install -y pcre-devel; yum -y clean all \  
&& mkdir -p /opt/swig/src \  
&& cd /opt/swig/src \  
&& wget
"https://downloads.sourceforge.net/project/swig/swig/swig-2.0.12/swig-2.0.12.tar.gz?r=&ts=1494449874&use_mirror=superb-
dca2" -O - \  
| tar xzf - \  
&& cd /opt/swig/src/swig-2.0.12 \  
&& ./configure --prefix=/usr/local/ \  
&& make \  
&& make install  
  
# Python dependencies  
RUN yum install -y hdf5-devel; yum -y clean all  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install virtualenv  
RUN virtualenv venv  
RUN source venv/bin/activate  
RUN pip install numpy scipy matplotlib astropy h5py healpy  
  
# GSL (latest version is not in RPM)  
RUN mkdir -p /opt/gsl/src \  
&& cd /opt/gsl/src \  
&& wget http://mirrors.ibiblio.org/gnu/ftp/gnu/gsl/gsl-1.16.tar.gz -O - \  
| tar xzf - \  
&& cd /opt/gsl/src/gsl-1.16 \  
&& ./configure --prefix=/usr/local/ \  
&& make \  
&& make install  
  
# FrameL  
RUN mkdir -p /opt/framel/src \  
&& cd /opt/framel/src/ \  
&& wget http://lappweb.in2p3.fr/virgo/FrameL/libframe-8.21.tar.gz -O - \  
| tar xzf - \  
&& cd /opt/framel/src/libframe-8.21 \  
&& ./configure --enable-swig-python --prefix=/usr/local/ \  
&& make \  
&& make install  
  
# MetaIO  
RUN mkdir -p /opt/metaio/src \  
&& cd /opt/metaio/src \  
&& wget http://software.ligo.org/lscsoft/source/metaio-8.4.0.tar.gz -O - \  
| tar xzf - \  
&& cd /opt/metaio/src/metaio-8.4.0 \  
&& ./configure --enable-swig-python --prefix=/usr/local/ \  
&& make \  
&& make install  
  
ENV
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:/usr/lib/pkgconfig:/usr/lib64/pkgconfig  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
CMD ["/bin/bash"]  

