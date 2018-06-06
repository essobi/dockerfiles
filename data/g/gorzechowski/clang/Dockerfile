FROM ubuntu:xenial  
  
RUN apt-get update && apt-get -y install software-properties-common  
  
# RUN add-apt-repository -y ppa:h-rayflood/llvm  
  
RUN apt-get update && apt-get -y --allow-unauthenticated install \  
clang-3.8 \  
make \  
cmake \  
subversion  
  
RUN ln -sf /usr/bin/clang++-3.8 /usr/bin/clang++ && ln -sf /usr/bin/clang-3.8
/usr/bin/clang  
  
RUN svn co --quiet http://llvm.org/svn/llvm-project/libcxx/trunk libcxx  
RUN export CXXFLAGS="-std=c++0x -stdlib=libc++"; cd libcxx/lib; \  
bash buildit && cp ./libc++.so.1.0 /usr/lib/; \  
mkdir /usr/include/c++/v1; cd ..; cp -r include/* /usr/include/c++/v1/; \  
cd /usr/lib; ln -sf libc++.so.1.0 libc++.so; ln -sf libc++.so.1.0 libc++.so.1  

