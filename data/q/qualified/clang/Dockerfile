FROM buildpack-deps:xenial  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
clang-3.8 \  
libc++-dev \  
; \  
update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.8 100; \  
update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.8
100; \  
curl -fsSL
https://github.com/Snaipe/Criterion/releases/download/v2.2.2/criterion-v2.2.2-linux-x86_64.tar.bz2
| tar xj -C /usr --strip-components=1; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/*;  
  
WORKDIR /workspace  
  
COPY rootfs/runner /runner  
COPY rootfs/usr /usr  
  
RUN set -ex; \  
cd /runner/frameworks/c; \  
clang -c criterion-hooks.c;  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

