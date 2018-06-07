# DOCKER-VERSION 1.1.0  
#inherit from the base container, which have all the needed script to launch
tasks  
FROM ingi/inginious-c-base  
LABEL org.inginious.grading.name="cpp"  
  
# Add gcc  
RUN yum install -y gcc gcc-c++ gdb cpp make cmake valgrind binutils libstdc++
clang clang-devel llvm automake check check-devel CUnit CUnit-devel zlib-devel
openssl-devel time jansson-devel && \  
yum clean all  

