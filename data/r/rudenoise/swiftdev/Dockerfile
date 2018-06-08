FROM rudenoise/nvimage:ubuntu-16.04  
  
RUN apt-get install -y \  
git \  
cmake \  
ninja-build \  
clang \  
uuid-dev \  
libicu-dev \  
icu-devtools \  
libbsd-dev \  
libedit-dev \  
libxml2-dev \  
libsqlite3-dev \  
swig \  
libpython-dev \  
libncurses5-dev \  
pkg-config \  
libblocksruntime-dev  
  
  
COPY ./install.bash /root/  
COPY ./vim.bash /root/  
  
RUN ./install.bash  

