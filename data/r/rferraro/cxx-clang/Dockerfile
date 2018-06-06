#rferraro/cxx-clang:3.9  
  
FROM rferraro/cxx-common:debian-sid  
  
ENV CC clang  
ENV CXX clang++  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
llvm-3.9 \  
clang-3.9 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.9 999 \  
&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.9
999 \  
&& update-alternatives --install /usr/bin/llvm-cov llvm-cov /usr/bin/llvm-
cov-3.9 999  

