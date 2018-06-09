FROM debian:testing  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --fix-missing cmake make g\\+\\+ clang-tools-6.0 perl
libssl-dev libboost-filesystem-dev libboost-context-dev libboost-coroutine-dev
libboost-thread-dev libasio-dev \  
&& apt-get autoremove -y \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/*  
  

