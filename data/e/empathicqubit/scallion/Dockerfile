FROM mono:5.8 AS build  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends clinfo libssl-dev curl tzdata && \  
apt-get remove mesa-* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /app  
  
RUN curl -s -L https://github.com/lachesis/scallion/archive/gpg.tar.gz | \  
tar --strip-components=1 -zxv  
  
RUN xbuild scallion.sln /p:TargetFrameworkVersion="v4.5"  
  
FROM nvidia/opencl:runtime AS run  
  
COPY --from=build /app /app  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends mono-runtime mono-xbuild clinfo
libssl1.0.0 && \  
apt-get remove mesa-* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/lib/x86_64-linux-gnu && \  
ln -s libOpenCL.so.1.0.0 libOpenCL.so && \  
cd /lib/x86_64-linux-gnu && \  
ln -s libcrypto.so.1.0.0 libcrypto.so && \  
ln -s libssl.so.1.0.0 libssl.so  
  
ENTRYPOINT ["mono", "/app/scallion/bin/Debug/scallion.exe"]  

