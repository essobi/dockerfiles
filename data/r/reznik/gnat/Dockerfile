FROM debian  
ENV
PATH=/opt/gnat/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN apt-get update && apt-get install -y \  
curl \  
libc-dev \  
make \  
&& curl -sSf http://mirrors.cdn.adacore.com/art/591c6d80c7a447af2deed1d7 \  
| tar xzf - -C /tmp \  
&& echo -e '\n/opt/gnat\ny\ny' | /tmp/gnat-gpl-2017-x86_64-linux-bin/doinstall
\  
; cd /opt/gnat \  
; gprinstall --uninstall gpr \  
&& gprinstall --uninstall aws \  
&& gprinstall --uninstall zfp_x86_64 \  
; cd /opt/gnat/lib/gnat/manifests \  
; rm -f `grep ^[0-9a-f] *|cut -d\ -f2` * \  
; cd /opt/gnat \  
; rm -rf bin/gnatdoc bin/gnatinspect bin/gps* etc include/py* \  
lib/girepository-1.0 lib/gps lib/gtk-3.0 lib/python2.7 \  
share/doc/gps share/examples/gps share/glib-2.0 share/gps \  
share/icons share/themes \  
&& find /opt/gnat/ -type d -empty -delete \  
&& rm -rf /tmp/gnat-gpl-2017-x86_64-linux-bin \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

