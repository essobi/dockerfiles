FROM calvintam236/ubuntu:amd  
  
MAINTAINER calvintam236 <calvintam236@users.noreply.github.com>  
LABEL description="XMRig-AMD in Docker. Supports GPU mining."  
  
WORKDIR /tmp  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install ca-certificates curl build-
essential cmake libmicrohttpd-dev libuv1-dev ocl-icd-opencl-dev \  
&& curl -L -O https://github.com/xmrig/xmrig-amd/archive/v2.6.1.tar.gz \  
&& tar -xvf v2.6.1.tar.gz \  
&& rm v2.6.1.tar.gz \  
&& cd xmrig-amd-2.6.1 \  
&& mkdir build \  
&& cd build \  
&& cmake .. \  
&& make \  
&& cd ../.. \  
&& mv xmrig-amd-2.6.1/build/xmrig-amd /usr/local/bin/xmrig-amd \  
&& chmod a+x /usr/local/bin/xmrig-amd \  
&& rm -r xmrig-amd-2.6.1 \  
&& apt-get -y remove ca-certificates curl build-essential cmake libmicrohttpd-
dev libuv1-dev ocl-icd-opencl-dev \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
ENTRYPOINT ["xmrig-amd"]  
CMD ["-h"]  

