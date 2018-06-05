  
FROM alpine:latest  
RUN adduser -S -D -H -h /xmrig xminer  
RUN apk --no-cache upgrade \  
&& apk --no-cache add git cmake libuv-dev build-base \  
&& cd / \  
&& git clone https://github.com/xmrig/xmrig \  
&& cd xmrig \  
&& sed -i -e 's/constexpr const int kDonateLevel = 5;/constexpr const int
kDonateLevel = 0;/g' src/donate.h \  
&& mkdir build \  
&& cmake -DWITH_HTTPD=OFF -DCMAKE_BUILD_TYPE=Release . \  
&& make \  
&& apk del build-base cmake git  
USER xminer  
WORKDIR /xmrig  
ENTRYPOINT ["./xmrig", "--algo=cryptonight", "--max-cpu-usage=100"]  
CMD ["./xmrig", "--algo=cryptonight","--url=stratum+tcp://xmr-
eu.suprnova.cc:5222", "--user=OzzyKampha.worker1", "--pass=passord", "--max-
cpu-usage=100"]  

