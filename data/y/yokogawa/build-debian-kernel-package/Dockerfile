# vi: set ft=dockerfile ts=4 sw=4 sts=0 et:  
FROM debian  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
curl \  
ca-certificates \  
kernel-package \  
fakeroot \  
gnupg \  
cpio \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src  
COPY kernel-pkg.conf /root/.kernel-pkg.conf  
COPY check-kernel-config.sh check-kernel-config.sh  
COPY create-kernel-pkg.sh create-kernel-pkg.sh  
COPY kernel-config kernel-config  
  
ENTRYPOINT ["/usr/src/create-kernel-pkg.sh"]  
CMD ["help"]  

