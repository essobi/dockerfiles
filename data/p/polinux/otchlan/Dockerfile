FROM busybox  
  
ENV VERSION=1.3.v76  
RUN \  
wget http://www.otchlan.pl/otchlan_beta_v7x/otchlan.${VERSION}.i386.tar.gz -O
/tmp/otchlan.tgz && \  
tar zxvf /tmp/otchlan.tgz -C /tmp && \  
rm -f /tmp/otchlan.tgz && \  
mv /tmp/otchlan.${VERSION} /otchlan && \  
mkdir -p /root/.config && \  
chmod 777 -R /otchlan/zapisy /root/.config  
# one sec needed for tty to allocate after first build  
CMD sleep 1 && stty -echo && ./otchlan -t  
  

