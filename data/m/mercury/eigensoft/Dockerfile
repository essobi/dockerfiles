FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
make \  
git \  
ca-certificates \  
gcc \  
build-essential \  
gfortran \  
libgsl0-dev \  
libopenblas-base \  
libopenblas-dev \  
liblapacke-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Compile EIG  
RUN git clone \--depth 1 --branch master https://github.com/DReichLab/EIG
/tmp/EIG  
WORKDIR /tmp/EIG/src  
ADD Makefile.patch Makefile.patch  
RUN patch < Makefile.patch  
RUN make clobber OPENBLAS=/opt/openblas \  
&& make install OPENBLAS=/opt/openblas \  
&& mv ../bin/* /usr/local/bin  
  
# Tidy up  
RUN rm -rf /tmp/*  
  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

