FROM debian:stretch  
  
# add unstable repositoty to install clang-format-5.0  
RUN echo -n 'deb http://ftp.debian.org/debian unstable main contrib non-free'
>> /etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
git curl cmake bc automake libtool build-essential pkg-config make \  
ca-certificates devscripts python unzip libllvm3.9 llvm-3.9-dev opencl-c-
headers \  
g++-6 clang-3.9 ocl-icd-opencl-dev ocl-icd-dev clang-format-5.0 diffutils \  
&& apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# add clang-format  
RUN update-alternatives --install /usr/bin/clang-format clang-format
/usr/bin/clang-format-5.0 11  

