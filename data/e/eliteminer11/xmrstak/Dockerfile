FROM alpine:latest  
  
RUN apk --no-cache upgrade \  
&& apk --no-cache add \  
git \  
cmake \  
automake \  
autoconf \  
build-base \  
openssl-dev \  
libmicrohttpd-dev \  
&& git clone https://github.com/fireice-uk/xmr-stak.git \  
&& cd xmr-stak \  
&& printf "#pragma once\nconstexpr double fDevDonationLevel = 0.0 / 100.0;" \  
> ./xmrstak/donate-level.hpp \  
&& cmake . \  
-DCUDA_ENABLE=OFF \  
-DOpenCL_ENABLE=OFF \  
-DHWLOC_ENABLE=OFF \  
&& make \  
&& cd - \  
&& mv /xmr-stak/bin/* /usr/local/bin/ \  
&& rm -rf /xmr-stak \  
&& apk del \  
git \  
automake \  
autoconf \  
build-base \  
&& cp /usr/local/bin/xmr-stak /xmrstak  
  
  
CMD ["/xmrstak]

