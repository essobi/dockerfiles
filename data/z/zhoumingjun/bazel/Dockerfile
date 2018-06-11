FROM zhoumingjun/dev-essential  
  
MAINTAINER zhoumingjun <zhoumingjun@gmail.com>  
  
# compile bazel  
RUN git clone https://github.com/google/bazel.git /opt/bazel && \  
/opt/bazel/compile.sh  
  
#add bazel  
ENV PATH $PATH:/opt/bazel/output/  
  
RUN cd /opt/bazel && \  
bazel build //scripts:bazel-complete.bash && \  
cp bazel-bin/scripts/bazel-complete.bash /etc/bash_completion.d  

