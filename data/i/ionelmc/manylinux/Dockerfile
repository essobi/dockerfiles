FROM quay.io/pypa/manylinux1_x86_64  
  
RUN yum install -y libffi-devel libmagic-devel libzlib-devel
libfreetype6-devel \  
libpng-devel libxml2-devel libxslt-devel expect-devel liblzma-devel \  
libenchant-devel libpq-devel libz-devel \  
strace gdb lsof locate net-tools htop iputils-ping dnsutils \  
&& rm /opt/python/cp26-*  
RUN for variant in /opt/python/*; do $variant/bin/pip install cffi==1.11.2
pycparser==2.18; done \  
&& rm -rf /root/.cache/pip  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

