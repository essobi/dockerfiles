FROM ubuntu:artful  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
RUN apt-get install --no-install-recommends -y clang libc++-dev libc++abi-dev  
RUN apt-get install --no-install-recommends -y make cmake  
  
RUN apt-get autoremove  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang 30  
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 30  
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-libc++ 40  
  
RUN update-alternatives --auto cc  
RUN update-alternatives --auto c++  
  
RUN update-alternatives --display cc  
RUN update-alternatives --display c++  
  
RUN cc --version  
RUN c++ --version  
  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
RUN echo '#include <functional> ' >> temp.cpp && \  
echo '#include <iostream> ' >> temp.cpp && \  
echo '#include <memory> ' >> temp.cpp && \  
echo 'class Foo final ' >> temp.cpp && \  
echo '{ ' >> temp.cpp && \  
echo 'public: ' >> temp.cpp && \  
echo ' auto Fn() noexcept -> void ' >> temp.cpp && \  
echo ' { ' >> temp.cpp && \  
echo ' } ' >> temp.cpp && \  
echo '}; ' >> temp.cpp && \  
echo 'int main() ' >> temp.cpp && \  
echo '{ ' >> temp.cpp && \  
echo ' using Proc = std::function<auto () -> void>; ' >> temp.cpp && \  
echo ' auto foo = std::make_shared<Foo>(); ' >> temp.cpp && \  
echo ' Proc f = std::bind(&Foo::Fn, foo); ' >> temp.cpp && \  
echo ' f(); ' >> temp.cpp && \  
echo ' return 0; ' >> temp.cpp && \  
echo '} ' >> temp.cpp && \  
c++ -xc++ -std=c++1z temp.cpp -o temp.out && \  
./temp.out && \  
rm -f temp.cpp temp.out  

