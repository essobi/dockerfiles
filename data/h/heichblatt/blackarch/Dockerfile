FROM heichblatt/archlinux-yaourt  
MAINTAINER heichblatt  
  
ENV SHA256SUM a3078417cc21e0e3e6fd352f1e4b790f7f94adf5422aa00e2c43d7b9fc493a9e  
USER root  
  
RUN cd /tmp/ && \  
/usr/bin/curl -O https://raw.githubusercontent.com/BlackArch/blackarch-
site/master/strap.sh && \  
echo ${SHA256SUM}" strap.sh" | sha256sum -c - && \  
/usr/bin/chmod +x ./strap.sh && \  
./strap.sh && \  
/usr/bin/rm -v /tmp/strap.sh && \  
/usr/bin/pacman -Scc --noconfirm  
USER user  
CMD ["/usr/bin/bash"]  

