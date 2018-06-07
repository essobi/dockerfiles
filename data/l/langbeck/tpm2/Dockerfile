## BEGIN OF SHARED REGION #############  
FROM ubuntu:xenial  
  
ARG https_proxy  
ARG http_proxy  
  
# NOTE: This is a common layer shared with some Dockerfile's  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ca-certificates \  
libssl-dev \  
curl \  
make \  
gcc \  
vim  
  
ENV PATH=/tpm2/src:$PATH  
WORKDIR tpm2  
  
# IBM's Software TPM 2.0  
RUN curl -L https://sourceforge.net/projects/ibmswtpm2/files/ibmtpm974.tar.gz
|\  
tar -xz &&\  
make -j4 -C src  
  
## END OF SHARED REGION ###############  
# Packages required by Intel projects  
RUN apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev \  
autoconf-archive \  
libglib2.0-dev \  
libdbus-1-dev \  
pkg-config \  
autoconf \  
automake \  
libtool \  
curl \  
man \  
git  
  
RUN git clone https://github.com/intel/tpm2-tss.git &&\  
cd tpm2-tss &&\  
./bootstrap &&\  
./configure --prefix=/usr &&\  
make -j4 &&\  
make install  
  
RUN git clone https://github.com/intel/tpm2-tools.git &&\  
cd tpm2-tools &&\  
./bootstrap &&\  
./configure --prefix=/usr &&\  
make -j4 &&\  
make install  
  
RUN git clone https://github.com/intel/tpm2-abrmd.git &&\  
cd tpm2-abrmd &&\  
./bootstrap &&\  
./configure --prefix=/ &&\  
make -j4 &&\  
make install  
  
# FIXME: For some misterious reason, dbus can't be installed in that previous  
# "apt-get install" up there. If we try to do so, tpm2-tools build breaks.  
RUN apt-get install -y --no-install-recommends dbus  
  
ADD bootstrap.sh /bootstrap.sh  
ENTRYPOINT ["/bootstrap.sh"]  

