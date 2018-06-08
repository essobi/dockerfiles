FROM debian:8  
MAINTAINER Serge at abrikus@gmail.com  
  
RUN apt-get update && \  
apt-get install --no-install-recommends wget ca-certificates sudo equivs gawk
nfs-common openssh-client -y && \  
wget https://github.com/sergevs/abt/releases/download/3.1.2/abt_3.1.2_all.deb
&& \  
dpkg -i abt_3.1.2_all.deb ; \  
apt-get install --no-install-recommends -fy && \  
rm -f abt_3.1.2_all.deb && \  
apt-get remove mawk awk -y && \  
apt-get clean && \  
echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
COPY user.init /usr/bin/  
  
ENTRYPOINT ["/usr/bin/user.init"]  

