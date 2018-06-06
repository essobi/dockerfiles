FROM centos:latest  
  
# Required packages for developing compilers  
RUN yum -y install gcc-c++ musl-dev make bison flex flex-devel llvm llvm-devel
llvm-static  
  
# symbolic link for libz for llvm  
RUN ln -s /usr/lib64/libz.so.1 /usr/lib64/llvm/libz.so  
# p4exe is looking for libffi.so.5  
RUN ln -s /usr/lib64/libffi.so /usr/lib64/libffi.so.5  
  
# Optional packages  
RUN yum -y install python  

