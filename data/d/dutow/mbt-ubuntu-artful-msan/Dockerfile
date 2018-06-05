# A simple dockerfile for building MySQL / Percona server  
# Source and build directories should be mounted under work  
# Use with the work-with script  
# This file is intended for building it with MSAN  
# Currently this requires either a custom built clang (not included in this
image),  
# or a workoround commit in the sources to fix an initialization crash.  
  
FROM dutow/mbt-ubuntu-artful  
MAINTAINER Zsolt Parragi <zsolt.parragi@cancellar.hu>  
  
ENV CPLUS_INCLUDE_PATH=/work/libcxx-msan-trunk/include/c++/v1 \  
C_INCLUDE_PATH=/work/libcxx-msan-trunk/include/c++/v1 \  
CC=/work/llvm/bin/clang \  
CXX=/work/llvm/bin/clang++ \  
CFLAGS=-fsanitize=memory \  
CXXFLAGS="-fsanitize=memory -Wno-unused-command-line-argument -nostdinc++
-stdlib=libc++" \  
LIBRARY_PATH=/work/libcxx-msan-trunk/lib:/work/llvm-
inst/lib:/work/llvm/lib/clang/7.0.0/lib/linux/ \  
LD_LIBRARY_PATH=/work/libcxx-msan-trunk/lib:/work/llvm-
inst/lib:/work/llvm/lib/clang/7.0.0/lib/linux/ \  
MSAN_OPTIONS="allocator_may_return_null=1"  

