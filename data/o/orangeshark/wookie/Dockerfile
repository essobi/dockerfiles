FROM ubuntu:14.04  
MAINTAINER Erik Edrosa <erik.edrosa@gmail.com>  
  
ENV LIBUV_VERSION v1.5.0  
ENV LIBUV_DIR libuv-$LIBUV_VERSION  
ENV LIBUV_ARCHIVE $LIBUV_DIR.tar.gz  
  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get install -y \  
sbcl \  
curl \  
make \  
automake \  
libtool \  
gcc  
  
WORKDIR /tmp/  
  
# download and build libuv for wookie  
RUN mkdir -p libuv \  
&& cd libuv \  
&& curl -sLO http://dist.libuv.org/dist/$LIBUV_VERSION/$LIBUV_ARCHIVE \  
&& tar xf $LIBUV_ARCHIVE \  
&& rm $LIBUV_ARCHIVE \  
&& cd $LIBUV_DIR \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf libuv  
  
# download and install quicklisp  
RUN curl -sO https://beta.quicklisp.org/quicklisp.lisp \  
&& echo "(load \"quicklisp.lisp\") (quicklisp-quickstart:install :path
\"/opt/quicklisp\") (ql::without-prompting (ql:add-to-init-file))" | sbcl \  
&& cp $HOME/.sbclrc /etc/sbclrc  
  
# download and install wookie  
RUN echo "(ql:quickload :wookie)" | sbcl  

