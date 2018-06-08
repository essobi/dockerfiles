FROM yusekiya/research-python  
  
WORKDIR "/tmp"  
  
RUN apt-get update && apt-get install -y build-essential cmake pkg-config
unzip &&\  
apt-get clean  
  
RUN \  
# Install fmtlib/fmt  
/usr/bin/curl -fsSL -o /tmp/fmt-4.0.0.zip
https://github.com/fmtlib/fmt/releases/download/4.0.0/fmt-4.0.0.zip &&\  
cd /tmp && /usr/bin/unzip -qq fmt-4.0.0.zip && cd fmt-4.0.0 &&\  
mkdir build && cd build && cmake ../ && make install && cd /tmp &&\  
# Install Eigen3  
/usr/bin/curl -fsSL -o /tmp/eigen3.tar.gz2
http://bitbucket.org/eigen/eigen/get/3.3.4.tar.bz2 &&\  
mkdir -p /tmp/eigen3/build && tar xf /tmp/eigen3.tar.gz2 -C /tmp/eigen3
\--strip-components 1 &&\  
cd /tmp/eigen3/build && cmake ../ && make install && cd /tmp &&\  
# Clean up  
rm -rf /tmp/*  
  
RUN conda install -yq -c conda-forge pybind11=2.2.1 &&\  
conda install -yq -c intel mkl-include mkl-static  
  
WORKDIR "/project"  

