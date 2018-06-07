# Docker image with Haskell libraries for GPU programming  
  
FROM mchakravarty/parallel-haskell:lts-1.4  
  
MAINTAINER Manuel M T Chakravarty <chak@justtesting.org>  
  
ENV PKGS accelerate-cuda-0.15.0.0 accelerate-fft-0.15.0.0  
# FIXME: 'accelerate-cublas' doesn't install as the 'cublas' package fails to
compile as it doesn't find the CUBLAS headers  
# even with --extra-include-dirs=/usr/local/cuda/include \--extra-lib-
dirs=/usr/local/cuda/lib64 explicitly  
# provided  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends g++ \  
&& curl -LS
http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_linux_64.run
>cuda.run \  
&& /bin/sh cuda.run \--extract=`pwd` \  
&& ./NVIDIA-Linux-x86_64-340.29.run -s -N \--no-kernel-module \  
&& ./cuda-linux64-rel-6.5.14-18749181.run \--noprompt \  
&& echo /usr/local/cuda/lib64 >/etc/ld.so.conf.d/cuda.conf \  
&& ldconfig \  
&& rm -rf *.run /usr/local/cuda/doc /usr/local/cuda/jre
/usr/local/cuda/libnsight /usr/local/cuda/libnvvp \  
&& curl -LS https://github.com/mchakravarty/mainland-pretty/archive/mainland-
pretty-0.2.8-mchakravarty.tar.gz \  
| tar -xz \  
&& (cd mainland-pretty-mainland-pretty-0.2.8-mchakravarty && cabal install) \  
&& rm -rf mainland-pretty-mainland-pretty-0.2.8-mchakravarty \  
&& cabal install $PKGS  
  
ENV PATH /usr/local/cuda/bin:$PATH  

