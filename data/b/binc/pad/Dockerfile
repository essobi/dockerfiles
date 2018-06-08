#  
# Dockerfile for the build/flash system for Poplar Andriod  
#  
FROM ubuntu:14.04  
MAINTAINER Bin Chen <bin.chen@linaro.org>  
  
RUN \  
fetchDeps='ca-certificates wget python android-tools-fsutils' && \  
apt-get update && \  
apt-get install -y --no-install-recommends $fetchDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /poplar  
COPY tools/mkimage /usr/bin  
VOLUME ["/poplar/flash_input", "/poplar/flash_output"]  
WORKDIR /poplar  
RUN wget -nv -O uflash.py
http://raw.githubusercontent.com/pierrchen/pat/master/uflash.py  
  
ENTRYPOINT ["python", "uflash.py", "-i", "/poplar/flash_input", "-o",
"/poplar/flash_output"]  
  
# default to all Android partitions, specify specific on when running the
container  
CMD []  

