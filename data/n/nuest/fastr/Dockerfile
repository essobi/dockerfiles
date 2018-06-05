# Based on https://github.com/graalvm/fastr#building-fastr-from-source  
FROM openjdk:9-jdk  
  
RUN sed -i "s/deb.debian.org/cdn-fastly.deb.debian.org/" /etc/apt/sources.list
\  
&& sed -i "s/security.debian.org/cdn-fastly.debian.org\/debian-security/"
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
gfortran \  
libpcre3-dev \  
libreadline-dev \  
zlib1g-dev \  
libbz2-dev \  
liblzma-dev \  
libcurl4-openssl-dev \  
ed \  
libmpc-dev \  
libssl-dev \  
&& ldconfig  
  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu/  
  
ENV FASTR_HOME=/fastr  
ENV MX_HOME=/usr/mx  
ENV PATH=$MX_HOME:$PATH  
  
# See
https://github.com/oracle/graal/blob/master/compiler/src/org.graalvm.compiler.hotspot/src/org/graalvm/compiler/hotspot/JVMCIVersionCheck.java  
#ENV JVMCI_VERSION_CHECK=ignore  
WORKDIR $FASTR_HOME  
  
# based on https://github.com/oracle/fastr#building-fastr-from-source  
RUN git clone \--depth 1 -b master https://github.com/graalvm/mx.git $MX_HOME
\  
&& git clone \--depth 1 https://github.com/oracle/fastr $FASTR_HOME \  
&& mx build  
  
# https://github.com/oracle/fastr/issues/11#issuecomment-389490445  
WORKDIR /graal/compiler  
RUN mx build  
  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
ARG GNUR_VERSION  
LABEL org.label-
schema.license="https://raw.githubusercontent.com/graalvm/fastr/master/LICENSE"
\  
org.label-schema.vendor="FastR project team, Dockerfile provided by Daniel
Nüst" \  
org.label-schema.name="FastR" \  
org.label-schema.description="FastR is an implementation of the R Language in
Java atop Truffle, a framework for building self-optimizing AST interpreters."
\  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.fastr.version="devel" \  
org.gnur.version=$GNUR_VERSION \  
org.label-schema.schema-version="rc1" \  
maintainer="Daniel Nüst <daniel.nuest@uni-muenster.de>"  
WORKDIR $FASTR_HOME  
ENV LANG=en_US.UTF-8  
ENTRYPOINT [ "mx", "--dynamicimports", "graal/compiler", "R" ]  
# enable compilation logs with mx --dynamicimport graal/compiler --J
"@-Dgraal.TraceTruffleCompilation=true" R  

