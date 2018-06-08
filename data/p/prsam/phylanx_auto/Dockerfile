FROM prsam/hpx_auto:master-debug  
  
RUN apt-get update && \  
apt-get install \--yes \--no-install-recommends \  
python3 \  
python3-dev \  
python3-pip \  
libblas-dev \  
liblapack-dev \  
libhdf5-dev && \  
apt-get purge && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN pip3 \--no-cache-dir install setuptools && \  
pip3 \--no-cache-dir install pytest && \  
pip3 \--no-cache-dir install numpy && \  
pip3 \--no-cache-dir install flake8  
  
# pybind  
RUN git clone \--depth=1 https://github.com/pybind/pybind11.git /pybind11 && \  
mkdir -p /pybind11/build && \  
cd /pybind11/build && cmake -DCMAKE_BUILD_TYPE=Release -DPYBIND11_TEST=OFF ..
&& \  
make -C /pybind11/build install && \  
rm -rf /pybind11  
# Blaze  
RUN git clone \--depth=1 https://bitbucket.org/blaze-lib/blaze.git /blaze && \  
mkdir -p /blaze/build && \  
cd /blaze/build && cmake -DCMAKE_BUILD_TYPE=Release -DBLAZE_SMP_THREADS=C++11
.. && \  
make -C /blaze/build install && \  
rm -rf /blaze  
# HighFive  
RUN git clone \--depth=1 https://github.com/BlueBrain/HighFive.git /highfive
&& \  
mkdir -p /highfive/build && \  
cd /highfive/build && cmake -DCMAKE_BUILD_TYPE=Release -DUSE_BOOST=Off .. && \  
make -C /highfive/build install && \  
rm -rf /highfive  
# Phylanx itself  
RUN export N_CORES=$(grep -c ^processor /proc/cpuinfo) && \  
git clone \--depth=1 https://github.com/STEllAR-Group/phylanx /phylanx && \  
mkdir -p /phylanx/build && \  
cd phylanx/build && cmake -DCMAKE_BUILD_TYPE=Debug \  
-DPHYLANX_WITH_GIT_COMMIT=$(git rev-parse HEAD) \   
-DPHYLANX_WITH_TOOLS=On \   
-DHPX_DIR=/usr/local/lib/cmake/HPX \   
-Dblaze_DIR=/blaze/share/blaze/cmake \   
-DPHYLANX_WITH_HIGHFIVE=On .. && \   
make -C /phylanx/build -j$N_CORES tools.inspect && \  
make -C /phylanx/build -j$N_CORES && \  
make -C /phylanx/build -j$N_CORES install && \  
rm -rf /phylanx/build && \  
ldconfig  

