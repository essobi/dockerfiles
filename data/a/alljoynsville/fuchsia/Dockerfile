FROM ubuntu:xenial  
  
MAINTAINER alljoynsville  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yqq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -yqq install texinfo libglib2.0-dev
autoconf \  
libtool libsdl-dev build-essential golang git curl unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /home/  
RUN curl -s https://raw.githubusercontent.com/fuchsia-
mirror/jiri/master/scripts/bootstrap_jiri | bash -s fuchsia  
WORKDIR /home/fuchsia  
ENV PATH /home/fuchsia/.jiri_root/bin:$PATH  
RUN jiri import fuchsia https://fuchsia.googlesource.com/manifest  
RUN jiri update  
RUN bash -c "source scripts/env.sh && envprompt && fset x86-64 --no-goma --no-
ccache && fbuild"  

