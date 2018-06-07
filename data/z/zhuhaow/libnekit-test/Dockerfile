FROM rikorose/gcc-cmake:gcc-5  
  
RUN apt-get update && apt-get install -y --no-install-recommends valgrind
libc6-dev-i386\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*

