###  
# Build image  
###  
#FROM alpine:edge AS build  
FROM alpine:edge  
  
ENV XMR_STAK_CPU_VERSION v1.3.0-1.5.0  
COPY app /app  
  
WORKDIR /usr/local/src  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
//etc/apk/repositories  
RUN apk add --no-cache \  
libmicrohttpd-dev \  
openssl-dev \  
hwloc-dev@testing \  
build-base \  
cmake \  
coreutils \  
git  
  
RUN git clone https://github.com/fireice-uk/xmr-stak-cpu.git \  
&& cd xmr-stak-cpu \  
&& git checkout -b build ${XMR_STAK_CPU_VERSION} \  
&& sed -i 's/constexpr double fDevDonationLevel.*/constexpr double
fDevDonationLevel = 0.0;/' donate-level.h \  
\  
&& cmake -DCMAKE_LINK_STATIC=ON . \  
&& make -j$(nproc) \  
\  
&& cp -t /app bin/xmr-stak-cpu config.txt \  
&& chmod 777 -R /app  
RUN apk del --no-cache --purge \  
libmicrohttpd-dev \  
openssl-dev \  
hwloc-dev@testing \  
build-base \  
cmake \  
coreutils \  
git || echo "apk purge error ignored"  
  
###  
# Deployed image  
###  
#FROM alpine:edge  
WORKDIR /app  
  
#RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
//etc/apk/repositories  
RUN apk add --no-cache \  
libmicrohttpd \  
openssl \  
hwloc@testing \  
python2 \  
py2-pip \  
&& pip install envtpl  
  
#COPY --from=build app .  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["xmr-stak-cpu"]  
  

