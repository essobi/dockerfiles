FROM fedora:24  
RUN dnf install -y \  
createrepo-0.10.3-3.fc21 \  
rpm-ostree-2016.9-1.fc24 \  
git \  
tar-2:1.28-7.fc24 \  
patch-2.7.5-3.fc24 \  
which-2.20-13.fc24 \  
&& dnf clean all && rm -rf /var/cache/dnf  

