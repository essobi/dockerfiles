FROM buildpack-deps:jessie  
MAINTAINER papaeye@gmail.com  
  
RUN gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 7C207910  
  
ENV EMACS_VERSION 24.5  
RUN mkdir -p /usr/src/emacs \  
&& curl -sSL -o emacs.tar.xz
http://ftpmirror.gnu.org/emacs/emacs-$EMACS_VERSION.tar.xz \  
&& curl -sSL -o emacs.tar.xz.sig
http://ftpmirror.gnu.org/emacs/emacs-$EMACS_VERSION.tar.xz.sig \  
&& gpg --verify emacs.tar.xz.sig \  
&& tar -xJC /usr/src/emacs --strip-components=1 -f emacs.tar.xz \  
&& rm emacs.tar.xz* \  
&& cd /usr/src/emacs \  
&& ./configure \  
\--prefix=/opt/emacs \  
\--without-all \  
\--without-x \  
&& make -j$(nproc) bootstrap \  
&& make install \  
&& find /opt/emacs -name '*.elc' | sed 's/elc$/el/' | xargs rm \  
&& rm -rf /usr/src/emacs  
  
ENV PATH /opt/emacs/bin:$PATH  
  
ENV CASK_VERSION 8337237449446e186ccd5ade0b0dc8c6ea7bd728  
  
RUN mkdir /opt/cask \  
&& curl -sSL https://github.com/cask/cask/archive/$CASK_VERSION.tar.gz \  
| tar -xzC /opt/cask --strip-components=1  
  
ENV PATH /opt/cask/bin:$PATH  
  
# bootstrap  
RUN cask version  
  
CMD ["emacs"]  

