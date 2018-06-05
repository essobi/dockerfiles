FROM buildpack-deps:artful  
  
RUN dpkg --add-architecture i386  
  
RUN curl -sL http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -  
  
RUN echo "deb http://apt.llvm.org/stretch/ llvm-toolchain-stretch-6.0 main" >
/etc/apt/sources.list.d/llvm.list  
  
RUN apt-get update -yqq  
  
RUN apt-get install clang-6.0 libc++-dev python-dev python-pip cmake gcc-
multilib g++-multilib -yqq  
  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-6.0 100  
RUN update-alternatives --install /usr/bin/clang++ clang++
/usr/bin/clang++-6.0 100  
  
RUN pip install conan conan_package_tools  
  
ENV CC clang  
ENV CXX clang++  

