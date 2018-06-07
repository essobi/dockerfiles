# A disposable development environment for java, python, and c++  
FROM project5/base  
MAINTAINER benjamin.gemmill@gmail.com  
  
# clang repository from https://apt.llvm.org  
RUN apt-get update && apt-get install -y \  
software-properties-common curl \  
&& curl https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \  
&& apt-add-repository "deb http://apt.llvm.org/`lsb_release -cs`/ llvm-
toolchain-`lsb_release -cs`-6.0 main"  
  
RUN apt-get update && apt-get install -y \  
sudo \  
vim less bash-completion \  
iputils-ping lsof \  
git openssh-client rsync curl \  
default-jdk \  
#python python-dev python-pip \  
python3 python3-dev python3-pip \  
clang-6.0 lldb-6.0 lld-6.0 \  
cmake make ccache \  
# boost  
libssl-dev libz-dev \  
# thrift  
flex bison \  
# google-perftools  
autoconf automake libtool libunwind-dev  
  
# Git  
RUN git config --global credential.helper "cache --timeout=3600" \  
&& git config --global push.default simple \  
&& git config --global core.editor "vim"  
  
# JDK  
ENV JAVA_HOME /usr/lib/jvm/default-java  
  
# clang  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-6.0 1000
\  
&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-6.0
1000 \  
&& update-alternatives --install /usr/bin/lldb lldb /usr/bin/lldb-6.0 1000  
ENV CC=/usr/bin/clang  
ENV CXX=/usr/bin/clang++  
  
# Java IDE  
RUN curl -L
"https://data.services.jetbrains.com/products/download?platform=linuxWithoutJDK&code=IIC"
| tar xz && mv idea* /opt/idea \  
&& chmod -R a+w /opt/idea  
  
# Python IDE  
RUN curl -L
"https://data.services.jetbrains.com/products/download?platform=linux&code=PCC"
| tar xz && mv pycharm* /opt/pycharm \  
&& "/usr/bin/python3" "/opt/pycharm/helpers/pydev/setup_cython.py" build_ext
--inplace \  
#&& "/usr/bin/python" "/opt/pycharm/helpers/pydev/setup_cython.py" build_ext
--inplace \  
&& chmod -R a+w /opt/pycharm  
  
# C++ IDE  
RUN curl -L
"https://data.services.jetbrains.com/products/download?platform=linux&code=CL"
| tar xz && mv clion* /opt/clion \  
&& "/usr/bin/python3"
"/opt/clion/plugins/python/helpers/pydev/setup_cython.py" build_ext --inplace
\  
#&& "/usr/bin/python"
"/opt/clion/plugins/python/helpers/pydev/setup_cython.py" build_ext --inplace
\  
&& chmod -R a+w /opt/clion  
  
# SQL IDE  
RUN curl -L "http://dbeaver.jkiss.org/files/dbeaver-ce-latest-
linux.gtk.x86_64.tar.gz" | tar xz \  
&& mv dbeaver /opt/dbeaver && chmod a+x /opt/dbeaver/dbeaver \  
&& chmod -R a+w /opt/dbeaver  
  
# Start up the IDEs like this once you're in.  
#/opt/idea/bin/idea.sh > /dev/null 2>&1  
#/opt/pycharm/bin/pycharm.sh > /dev/null 2>&1  
#/opt/clion/bin/clion.sh > /dev/null 2>&1  
#/opt/dbeaver/dbeaver > /dev/null 2>&1  

