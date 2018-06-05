FROM debian:unstable  
  
MAINTAINER Sysdig <support@sysdig.com>  
  
ENV SYSDIG_REPOSITORY dev  
  
ENV SYSDIG_HOST_ROOT /host  
  
ENV HOME /root  
  
RUN cp /etc/skel/.bashrc /root && cp /etc/skel/.profile /root  
  
ADD http://download.draios.com/apt-draios-priority /etc/apt/preferences.d/  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
bash-completion \  
bc \  
clang-7 \  
curl \  
gnupg2 \  
ca-certificates \  
gcc \  
gcc-6 \  
gcc-5 \  
libc6-dev \  
libelf-dev \  
libelf1 \  
llvm-7 \  
openjdk-8-jre-headless \  
python bzip2 && rm -rf /var/lib/apt/lists/*  
# Since our base Debian image ships with GCC 7 which breaks older kernels,
revert the  
# default to gcc-5.  
# Older distributions of Debian use hardcoded versions of gcc in the kernel
Makefile. We  
# pretend to have them by creating symlinks to our default gcc.  
# 4.9 is required for Debian Jessie+backports and 4.8 is required for Debian
Jessie.  
RUN rm -rf /usr/bin/gcc && ln -s /usr/bin/gcc-5 /usr/bin/gcc \  
&& ln -s /usr/bin/gcc /usr/bin/gcc-4.9 \  
&& ln -s /usr/bin/gcc /usr/bin/gcc-4.8  
  
RUN rm -rf /usr/bin/clang \  
&& rm -rf /usr/bin/llc \  
&& ln -s /usr/bin/clang-7 /usr/bin/clang \  
&& ln -s /usr/bin/llc-7 /usr/bin/llc  
  
RUN curl -s https://s3.amazonaws.com/download.draios.com/DRAIOS-GPG-KEY.public
| apt-key add - \  
&& curl -s -o /etc/apt/sources.list.d/draios.list
http://download.draios.com/$SYSDIG_REPOSITORY/deb/draios.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends draios-agent \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ln -s $SYSDIG_HOST_ROOT/lib/modules /lib/modules  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

