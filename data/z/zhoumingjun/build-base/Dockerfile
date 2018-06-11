FROM zhoumingjun/dev-essential  
  
MAINTAINER zhoumingjun <zhoumingjun@gmail.com>  
  
#======================== bazel ==============================  
RUN git clone https://github.com/google/bazel.git /opt/bazel && \  
cd /opt/bazel && \  
git checkout 91430c71b && \  
/opt/bazel/compile.sh  
  
#add bazel  
ENV PATH $PATH:/opt/bazel/output/  
  
RUN cd /opt/bazel && \  
bazel build //scripts:bazel-complete.bash && \  
cp bazel-bin/scripts/bazel-complete.bash /etc/bash_completion.d  
  
  
#======================== thrift ==============================  
RUN git clone https://github.com/apache/thrift.git /opt/thrift && \  
sed -i 's/lua_rawlen/lua_objlen/g' /opt/thrift/lib/lua/src/luabpack.c && \  
cd /opt/thrift && \  
./bootstrap.sh && \  
./configure && \  
make && \  
cp /opt/thrift/lib/lua/.libs/* /usr/local/lib && \  
make install  

