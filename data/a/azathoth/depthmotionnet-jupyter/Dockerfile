FROM jupyter/tensorflow-notebook  
  
USER root  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
cmake && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/lmb-freiburg/demon.git --recursive  
RUN cd demon/lmbspecialops && \  
mkdir build && \  
cd build && \  
cmake .. -DBUILD_WITH_CUDA=OFF && \  
make  
  
RUN pip install vtk  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
python3-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LD_LIBRARY_PATH=/opt/conda/lib/python3.6/site-
packages/vtk:$LD_LIBRARY_PATH  
  
ENV CFLAGS="-I /opt/conda/lib/python3.6/site-packages/numpy/core/include
$CFLAGS"  
ADD setup.py /home/jovyan/demon/python/depthmotionnet/setup.py  
  
RUN cd demon/python/depthmotionnet && \  
python setup.py build_ext --inplace  
  
USER $NB_USER  
  
# u spuštění vis funkcí nelze zkompilovat vis_cython.pyx, na to se musí přidat
proměnná  
# export CFLAGS="-I /opt/conda/lib/python3.6/site-packages/numpy/core/include
$CFLAGS"  
# a radši zkompilovat vis předem v dockerfilu  
# v demon/python/depthmotionnet vytvořím setup.py a pak zkompiluju příkazem
python setup.py build_ext --inplace  
# ale tu proměnnou CGFLAGS přidat předtím

