FROM ubuntu:trusty  
MAINTAINER Francesco Komauli <francesco.komauli@gmail.com>  
  
ENV COQBIN=/usr/local/bin/  
ENV PATH="$COQBIN:$PATH"  
ENV COQ_VERSION=v8.4  
ENV QUICKCHICK_VERSION=itp-2015-final  
ENV
SSREFLECT_SHA256=bad978693d1bfd0a89586a34678bcc244e3b7efba6431e0f83d8e1ae8f82a142  
  
VOLUME /coq  
  
RUN apt-get update && apt-get install -y \  
ocaml \  
camlp5 \  
proofgeneral \  
proofgeneral-doc \  
git \  
vim \  
wget \  
make \  
time  
  
WORKDIR /tmp  
RUN git clone -b $COQ_VERSION https://github.com/coq/coq.git  
WORKDIR /tmp/coq  
RUN ./configure -prefix /usr/local \  
&& make \  
&& make install  
  
WORKDIR /tmp  
RUN wget http://ssr.msr-inria.inria.fr/FTP/ssreflect-1.5.tar.gz \  
&& echo "$SSREFLECT_SHA256 ssreflect-1.5.tar.gz" | sha256sum -c - \  
&& tar -xzf ssreflect-1.5.tar.gz  
WORKDIR /tmp/ssreflect-1.5  
RUN make \  
&& make install  
  
WORKDIR /tmp  
RUN git clone https://github.com/QuickChick/QuickChick  
WORKDIR /tmp/QuickChick  
RUN git checkout $QUICKCHICK_VERSION \  
&& make \  
&& make install  
  
WORKDIR /tmp  
RUN rm -rf coq ssreflect-1.5 QuickChick  
  
USER root  
WORKDIR /coq  

