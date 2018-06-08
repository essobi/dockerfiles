FROM ubuntu:zesty  
RUN apt-get update && apt-get install libprotobuf-dev cmake clang-3.8
clang-3.9 g++-6 g++-5 g++-4.9 build-essential libboost-all-dev cmake-data
protobuf-compiler valgrind gdb curl git -yy  
RUN curl -sSfL https://github.com/htfy96/logbt/archive/2.0-alpha.tar.gz | tar
--gunzip --extract --strip-components=1 --exclude="*md" \--exclude="test*"
\--directory=/usr/local && ln -s /usr/local/bin/logbt /usr/bin/logbt  
CMD "/bin/bash"  

