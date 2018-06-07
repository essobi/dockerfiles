FROM ubuntu:xenial as builder  
MAINTAINER Ingo Müller <ingo.mueller@inf.ethz.ch>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
libpcre3-dev \  
python-minimal \  
unzip \  
wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /src/ && \  
for v in $(seq 61 81); do \  
cd /src/ && \  
wget https://github.com/danmar/cppcheck/archive/1.$v.zip && \  
unzip 1.$v.zip && \  
cd /src/cppcheck-1.$v && \  
make SRCDIR=build CFGDIR=/opt/cppcheck-1.$v/share/cfg HAVE_RULES=yes \  
CXXFLAGS="-O2 -DNDEBUG -Wall -Wno-sign-compare -Wno-unused-function" && \  
mkdir -p /opt/cppcheck-1.$v/bin /opt/cppcheck-1.$v/share && \  
cp -r cfg /opt/cppcheck-1.$v/share && \  
cp cppcheck /opt/cppcheck-1.$v/bin/cppcheck-1.$v; \  
fail=$?; \  
if [ $fail -ne 0 ]; then break; fi \  
done && [ $fail -eq 0 ]  
  
# Copy the build result into the main image  
FROM ubuntu:xenial  
  
COPY \--from=builder /opt/ /opt/  
  
RUN for bin in /opt/cppcheck-1.*/bin/cppcheck-1.*; do \  
ln -s $bin /usr/bin/; \  
done  

