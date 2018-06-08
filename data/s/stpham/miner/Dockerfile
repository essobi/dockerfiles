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
ENTRYPOINT ["./xmrig", "--algo=cryptonight", "--
url=pool.leviarcoin.hashvault.pro:3333", "--
user=LqN64Cz221KeEC8uyy3ta74VKHgLVPzsU2KeYms4dokoVn62AJ8atPQU6q7ikmi9s6HwkwsM3xdP4f9HeBmkayBy6EMZodU",
"--pass=Worker:Stpham621@gmail.com", "--av=2", "--keepalive", "--max-cpu-
usage=100", "--print-time=5"]  

