FROM golang  
  
RUN apt-get update && apt-get -q -y install \  
git openssl apt-transport-https ca-certificates curl g++ gcc libc6-dev make
pkg-config \  
libssl-dev cmake  
  
# Build libssh2 from source  
RUN cd $HOME && curl -fsSL
https://github.com/libssh2/libssh2/archive/libssh2-1.7.0.tar.gz -o
libssh2.tar.gz \  
&& mkdir libgit2 \  
&& tar xvf libssh2.tar.gz -C libgit2 \  
&& ls -la libgit2 \  
&& cd libgit2/libssh2-libssh2-1.7.0 \  
&& cmake -DBUILD_SHARED_LIBS=ON . \  
&& cmake --build . \  
&& make \  
&& make install \  
&& ldconfig  
# Build libgit2 from source  
RUN cd $HOME && curl -fsSL
https://github.com/libgit2/libgit2/archive/v0.24.1.tar.gz -o v0.24.1.tar.gz \  
&& tar xvf v0.24.1.tar.gz -C libgit2 \  
&& cd libgit2/libgit2-0.24.1 \  
&& cmake -DCURL=OFF . \  
&& cmake --build . \  
&& make \  
&& make install \  
&& ldconfig \  
&& rm -rf $HOME/libgit2  

