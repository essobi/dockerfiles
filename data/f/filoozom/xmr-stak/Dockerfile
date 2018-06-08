FROM alpine as builder  
  
RUN apk add --no-cache \  
git \  
build-base \  
openssl-dev \  
cmake \  
libstdc++ \  
&& cd / \  
&& git clone https://github.com/fireice-uk/xmr-stak.git app \  
&& mkdir app/build \  
&& cd app/build \  
&& sed -i 's/constexpr double fDevDonationLevel.*/constexpr double
fDevDonationLevel = 0.0;/' ../xmrstak/donate-level.hpp \  
&& cmake .. \  
-DCMAKE_BUILD_TYPE=Release \  
-DMICROHTTPD_ENABLE=OFF \  
-DOpenSSL_ENABLE=ON \  
-DXMR-STAK_CURRENCY=monero \  
-DXMR-STAK_COMPILE=native \  
-DCPU_ENABLE=ON \  
-DHWLOC_ENABLE=OFF \  
-DOpenCL_ENABLE=OFF \  
-DCUDA_ENABLE=OFF \  
-DCMAKE_INSTALL_PREFIX=/output \  
&& make  
  
FROM alpine  
  
RUN apk add --no-cache \  
openssl \  
libgcc \  
libstdc++  
  
COPY --from=builder /app/build/bin/xmr-stak .  
ENTRYPOINT ["./xmr-stak"]  
CMD ["-h"]

