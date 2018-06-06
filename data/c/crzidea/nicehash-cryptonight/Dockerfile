FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y \  
libmicrohttpd-dev \  
libssl-dev \  
cmake \  
build-essential \  
libhwloc-dev \  
git \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN git clone https://github.com/fireice-uk/xmr-stak-cpu.git  
  
RUN cd xmr-stak-cpu \  
&& sed -i 's/constexpr double fDevDonationLevel =.*/constexpr double
fDevDonationLevel = 0;/' donate-level.h \  
&& cmake . \  
&& make install \  
&& cp -r bin /usr/local  
  
ADD etc etc  
ADD entrypoint.sh entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

