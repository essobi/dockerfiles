FROM ubuntu:15.04  
MAINTAINER Rob "Bubba" Hines <rob@stechstudio.com>  
  
# Setup/Configure apt  
RUN apt-get update  
  
# Install packages  
# We install these first, so that apt doesn't complain too much with the
others  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y dialog apt-utils  
  
# Now, lets get all the packages we want  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
automake curl \  
build-essential \  
fftw3 \  
gettext \  
ghostscript \  
gobject-introspection \  
gtk-doc-tools \  
libcfitsio-dev \  
libexif-dev \  
libfftw3-dev \  
libgirepository1.0-dev \  
libglib2.0-dev \  
libgs-dev \  
libgsf-1-dev \  
libjpeg-turbo8-dev \  
liblcms2-dev \  
libmagickwand-dev \  
libmatio-dev \  
libopenslide-dev \  
liborc-0.4-dev \  
libpangoft2-1.0-0 \  
libpcre3-dev \  
libpng12-dev \  
libtiff5-dev \  
libwebp-dev \  
libxml2-dev \  
php5-cli \  
php5-common \  
php5-curl \  
php5-gd \  
php5-json \  
php5-mcrypt \  
pkg-config \  
poppler-utils \  
python \  
python-dev \  
python-gi-dev \  
python-gobject \  
swig  
  
# finally, we run this, and fix any missing  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y imagemagick --fix-
missing  
  
# Lets fetch the libvips source  
WORKDIR /tmp  
ENV LIBVIPS_VERSION_MAJOR 8  
ENV LIBVIPS_VERSION_MINOR 0  
ENV LIBVIPS_VERSION_PATCH 2  
ENV LIBVIPS_VERSION
$LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR.$LIBVIPS_VERSION_PATCH  
RUN curl -O
http://www.vips.ecs.soton.ac.uk/supported/$LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR/vips-$LIBVIPS_VERSION.tar.gz  
RUN tar zvxf vips-$LIBVIPS_VERSION.tar.gz  
  
# Now Build that Sucker!  
WORKDIR /tmp/vips-$LIBVIPS_VERSION  
RUN ./configure --enable-debug=no  
RUN make  
RUN make install  
RUN ldconfig  
  
# Lets setup Python Now  
ENV PYTHONPATH /usr/local/lib/python2.7/site-packages  
RUN cp /usr/local/lib/girepository-1.0/* /usr/lib/girepository-1.0/  
RUN cp /usr/local/lib/python2.7/site-packages/gi/overrides/Vips.py
/usr/lib/python2.7/dist-packages/gi/overrides/Vips.py  
  
# Fetch PIP & Install it  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
  
# Install those packages  
RUN pip install boto  
RUN pip install ghostscript  
RUN pip install iron_mq  
RUN pip install iron_worker  
RUN pip install python-magic  
RUN pip install twisted  
RUN pip install logentries  
  
# Clean up, get rid of no longer needed packages, etc.  
WORKDIR /  
RUN apt-get remove -y automake build-essential  
RUN apt-get autoremove -y  
RUN apt-get autoclean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

