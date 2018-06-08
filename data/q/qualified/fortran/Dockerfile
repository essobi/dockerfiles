FROM ubuntu:16.04  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
# Install GNU Fortran 95 compiler  
# https://packages.ubuntu.com/xenial/gfortran  
gfortran \  
wget \  
ca-certificates \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
# TODO decide how to make this official  
# https://github.com/Codewars/codewars-runner-cli/issues/553  
# https://github.com/DonaldKellett/fortran-kata  
RUN set -ex; \  
mkdir -p /runner/frameworks/fortran; \  
cd /runner/frameworks/fortran; \  
wget -q -O cw-2.f95 https://raw.githubusercontent.com/DonaldKellett/fortran-
kata/master/frameworks/fortran/cw-2.f95; \  
gfortran -c cw-2.f95; \  
rm cw-2.f95;  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
WORKDIR /workspace  

