FROM vtrinque/base  
  
MAINTAINER Valentin Trinque <val.trinque@gmail.com>  
  
# install instrumentation tools (profilers, debuggers...)  
USER root  
RUN yum clean all && yum update -y && yum install -y \  
gdb \  
lldb \  
valgrind  
  
USER app

