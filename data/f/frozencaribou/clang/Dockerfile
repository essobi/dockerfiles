  
FROM ubuntu:16.04  
MAINTAINER Frozen Caribou  
  
  
# Default command on startup.  
CMD bash  
  
# Setup packages.  
RUN apt-get update && apt-get -y install cmake git build-essential vim python  
  
# Install clang from repo to avoid step 0 build  
RUN apt-get install -y clang-3.6 llvm-3.6  
  
# Add clang, clang++, llvm-config symbolink link  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.6 10 ;
update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.6 10  
  
# Copy install-clang over.  
ADD . /opt/install-clang  
  
# Set a name and email to apply git patches  
RUN git config \--global user.name "test" ; git config \--global user.email
"test@test.test"  
# Compile and install LLVM/clang 3.6. We delete the source directory to  
# avoid committing it to the image.  
RUN /opt/install-clang/install-clang -k release_36 -j 4 -C /opt/llvm  
  
# Uninstall previous clang-3.6  
RUN apt-get remove -y clang-3.6 llvm-3.6  
  
# Setup environment.  
ENV PATH /opt/llvm/bin:$PATH  

