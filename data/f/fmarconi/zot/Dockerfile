FROM blitznote/debootstrap-amd64:16.04  
MAINTAINER Francesco Marconi <francesco.marconi@polimi.it>  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vendor="Politecnico di Milano" \  
org.label-schema.name="zot" \  
org.label-schema.version="HEAD" \  
org.label-schema.vcs-type="git" \  
org.label-schema.vcs-url="https://github.com/fm-polimi/zot" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0"  
# Setting the environment  
ENV USERHOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
ENV Z3_VERSION 4.5.0  
ENV TMP_BUILD_DEPS ca-certificates \  
gcc \  
g++ \  
make \  
zlib1g-dev  
  
ADD . /usr/local/zot/  
WORKDIR /tmp  
# Update the repos and install all the used packages  
RUN apt-get -q update && apt-get install -y --no-install-recommends \  
$TMP_BUILD_DEPS \  
libgomp1 \  
sbcl \  
&& rm -rf /var/lib/apt/lists/* \  
##  
# installing minisat  
&& curl -L http://minisat.se/downloads/minisat-2.2.0.tar.gz -o
/tmp/minisat-2.2.0.tar.gz \  
&& cd /tmp \  
&& tar -xvzf minisat-2.2.0.tar.gz \  
&& export MROOT=/tmp/minisat \  
&& cd minisat/core/ \  
&& make \  
&& cp minisat /usr/local/bin/minisat \  
&& make clean \  
##  
# installing z3  
&& curl -L
https://github.com/Z3Prover/z3/releases/download/z3-${Z3_VERSION}/z3-${Z3_VERSION}-x64-ubuntu-14.04.zip
-o /tmp/z3.zip \  
&& unzip /tmp/z3.zip -d /tmp \  
&& cp /tmp/z3-${Z3_VERSION}-x64-ubuntu-14.04/bin/z3 /usr/local/bin/z3 \  
&& chmod a+x /usr/local/bin/z3 \  
##  
# installing zot  
# && git clone https://github.com/fm-polimi/zot /usr/local/zot/ \  
&& mkdir /usr/lib/sbcl/site-systems/ \  
&& ln -s /usr/local/zot/asdfs/*.asd /usr/lib/sbcl/site-systems/ \  
&& cp /usr/local/zot/bin/zot /usr/local/bin/ \  
##  
# remove build deps  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $TMP_BUILD_DEPS \  
&& rm -rf /tmp  

