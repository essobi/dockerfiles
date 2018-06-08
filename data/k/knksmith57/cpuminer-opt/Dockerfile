FROM ubuntu:xenial as compiler  
  
RUN apt-get update \  
&& apt-get install -y \  
git build-essential libssl-dev libgmp-dev libcurl4-openssl-dev libjansson-dev
automake \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone \--recursive https://github.com/JayDDee/cpuminer-opt.git
/tmp/cpuminer-opt \  
&& cd /tmp/cpuminer-opt \  
&& ./build.sh  
  
FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y \  
libcurl3 libjansson4 \  
&& rm -rf /var/lib/apt-lists/*  
  
COPY \--from=compiler /tmp/cpuminer-opt/cpuminer /usr/local/bin/  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD []  

