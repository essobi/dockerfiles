FROM fedora:27  
RUN dnf install -y \  
bash \  
fio \  
git \  
maven \  
wget \  
xz \  
&& dnf clean all && \  
rm -rf /var/cache/yum && \  
useradd bench-runner  
  
RUN wget -O kernel.tar.xz
https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.1.51.tar.xz && \  
chmod 644 /kernel.tar.xz && \  
mkdir -p /target && \  
chmod 777 /target  
  
COPY entry.sh /  
RUN chmod 755 /entry.sh  
  
USER bench-runner:bench-runner  
  
ENTRYPOINT ["/entry.sh"]  

