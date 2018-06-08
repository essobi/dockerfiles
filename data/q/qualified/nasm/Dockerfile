FROM buildpack-deps:xenial  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
# 2.11.08-1  
nasm \  
binutils; \  
curl -fsSL
https://github.com/Snaipe/Criterion/releases/download/v2.2.2/criterion-v2.2.2-linux-x86_64.tar.bz2
| tar xj -C /usr --strip-components=1; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/*;  
  
WORKDIR /workspace  
  
COPY rootfs/runner /runner  
  
RUN cd /runner/frameworks/c && gcc -c criterion-hooks.c  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

