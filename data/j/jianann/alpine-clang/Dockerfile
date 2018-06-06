FROM alpine:latest  
  
RUN echo "ipv6" >> /etc/modules  
  
RUN apk update && apk upgrade  
  
RUN apk add --no-cache clang clang-dev alpine-sdk dpkg  
RUN apk add --update --no-cache cmake  
RUN apk add --update --no-cache ccache  
  
RUN ls -l /usr/bin/cc /usr/bin/c++ /usr/bin/clang /usr/bin/clang++  
  
RUN ln -sf /usr/bin/clang /usr/bin/cc  
RUN ln -sf /usr/bin/clang++ /usr/bin/c++  
  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang 10  
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 10  
  
RUN update-alternatives --auto cc  
RUN update-alternatives --auto c++  
  
RUN update-alternatives --display cc  
RUN update-alternatives --display c++  
  
RUN ls -l /usr/bin/cc /usr/bin/c++  
  
RUN cc --version  
RUN c++ --version  
  
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
c++ -xc++ -std=c++14 temp.cpp -o temp.out && \  
./temp.out && \  
rm -f temp.cpp temp.out  

