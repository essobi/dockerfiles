FROM heroku/cedar:14  
MAINTAINER Wataru MIYAGUNI <gonngo@gmail.com>  
  
RUN echo "deb-src http://archive.ubuntu.com/ubuntu trusty main" >>
/etc/apt/sources.list  
  
RUN apt-get update -qqy \  
&& apt-get -qqy build-dep \  
emacs24 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV EMACS_VERSION 24.5  
#  
# Install emacs to /app/emacs  
#  
RUN mkdir -p /app/emacs  
RUN curl -s --retry 3 -L
http://ftp.jaist.ac.jp/pub/GNU/emacs/emacs-$EMACS_VERSION.tar.gz | tar xz -C /
\  
&& cd /emacs-$EMACS_VERSION \  
&& ./configure \  
\--prefix=/app/emacs \  
\--without-xpm \  
\--without-jpeg \  
\--without-tiff \  
\--without-gif \  
\--without-png \  
\--without-rsvg \  
\--without-xml2 \  
\--without-imagemagick \  
\--without-xft \  
\--without-libotf \  
\--without-m17n-flt \  
\--without-toolkit-scroll-bars \  
\--without-xaw3d \  
\--without-xim \  
\--without-gpm \  
\--without-dbus \  
\--without-gconf \  
\--without-gsettings \  
\--without-selinux \  
\--without-sound \  
\--without-gnutls \  
\--without-zlib \  
\--without-makeinfo \  
\--without-x \  
&& make -s -j 4 \  
&& make -s install \  
&& rm -rf /emacs-$EMACS_VERSION  
  
#  
# Install Cask to /app/cask  
#  
RUN git clone https://github.com/cask/cask.git /app/cask  
  
RUN mkdir -p /app/user  
WORKDIR /app/user  
  
#  
# Run cask-install to cache dependencies  
#  
ENV PATH /app/emacs/bin:/app/cask/bin:$PATH  
ONBUILD COPY ./Cask /app/user/  
ONBUILD RUN cask install  
ONBUILD COPY . /app/user/  
  
#  
# Export environment variables that is read during startup  
#  
# See: https://devcenter.heroku.com/articles/profiled  
#  
RUN mkdir -p /app/.profile.d/  
RUN echo "export PATH=\"$PATH\"" > /app/.profile.d/path.sh  
  
#  
# Emulate the feature as describes above  
#  
COPY ./init.sh /init.sh  
RUN chmod +x /init.sh  
  
ENTRYPOINT ["/init.sh"]  

