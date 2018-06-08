FROM martbab/freeipa-fedora-builder:master-latest  
ENV container=docker LANG=en_US.utf8 LANGUAGE=en_US.utf8 LC_ALL=en_US.utf8  
  
RUN dnf copr enable -y @freeipa/freeipa-4-4 \  
&& dnf config-manager --set-disabled updates-testing \  
&& dnf install -y freeipa-server freeipa-server-dns \  
freeipa-server-trust-ad python-ipatests --best --allowerasing \  
&& dnf clean all \  
&& for i in /usr/lib/systemd/system/*-domainname.service; \  
do sed -i 's#^ExecStart=/#ExecStart=-/#' $i ; done  
  
STOPSIGNAL RTMIN+3  
VOLUME ["/freeipa", "/run", "/tmp"]  
ENTRYPOINT [ "/usr/sbin/init" ]  
  
# docker run -v /sys/fs/cgroup:/sys/fs/cgroup:ro --tmpfs /run --tmpfs /tmp -v  
# /dev/urandom:/dev/random:ro ${IMAGE}  

