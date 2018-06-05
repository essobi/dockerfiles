FROM nvidia/cuda:8.0-devel  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -y git vim sudo openssh-server
python-pip \  
python-virtualenv gcc gfortran binutils python-dev libffi-dev libzmq3-dev
locate  
  
# compile openmpi with cuda support  
#RUN wget https://www.open-
mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz  
RUN wget https://www.open-
mpi.org/software/ompi/v2.0/downloads/openmpi-2.0.0.tar.gz  
RUN tar xzf openmpi-2.0.0.tar.gz  
WORKDIR /openmpi-2.0.0  
RUN ./configure --with-cuda=/usr/local/cuda --prefix=/openmpi  
RUN make -j$(nproc) && make install  
# for cpu only environments  
RUN ./configure --prefix=/openmpi-cpu  
RUN make -j$(nproc) && make install  
  
# compile openblas  
WORKDIR /  
RUN git clone https://github.com/xianyi/OpenBLAS  
RUN cd OpenBLAS && make -j$(nproc) FC=gfortran && make PREFIX=/OpenBLAS
install  
RUN echo '/OpenBLAS/lib' > /etc/ld.so.conf.d/openblas.conf && ldconfig  
  
# dependency for numpy install  
RUN pip install cython  
  
# compile numpy with OpenBLAS support  
RUN git clone https://github.com/numpy/numpy  
RUN echo "[openblas]" >> numpy/site.cfg && \  
echo "libraries = openblas" >> numpy/site.cfg && \  
echo "library_dirs = /OpenBLAS/lib" >> numpy/site.cfg && \  
echo "include_dirs = /OpenBLAS/include" >> numpy/site.cfg && \  
echo "runtime_library_dirs = /OpenBLAS/lib" >> numpy/site.cfg  
  
RUN cd numpy && python setup.py config && \  
python setup.py build -j $(nproc) && python setup.py install  
  
# set environment for pip module install  
ENV PATH "/OpenBLAS/bin:/openmpi/bin:$PATH"  
ENV LD_LIBRARY_PATH "/OpenBLAS/lib:/openmpi/lib:$LD_LIBRARY_PATH"  
ENV CUDA_ROOT "/usr/local/cuda"  
ENV NOTVISIBLE "in users profile"  
# install other dependencies  
COPY ./requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
RUN git clone https://github.com/inducer/pycuda --recursive  
RUN cd pycuda && ./configure.py && make -j$(nproc) && make install  
  
RUN git clone https://github.com/lebedov/scikit-cuda  
RUN cd scikit-cuda && python setup.py install  
  
COPY ./requirements-gpu.txt requirements-gpu.txt  
RUN pip install -r requirements-gpu.txt  
  
# create a non-root user  
ENV USERNAME crow  
ENV HOME=/home/${USERNAME}  
  
USER root  
RUN useradd -s /bin/bash -m ${USERNAME}  
# change passwords  
RUN echo "${USERNAME}:${USERNAME}" | chpasswd  
  
RUN mkdir /var/run/sshd  
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen  
# Skipped for compatibility with automatic build && locale-gen  
# Set environment variables  
#RUN echo '. /etc/profile.d/crow.sh' >> /etc/bash.bashrc  
RUN echo 'export VISIBLE=now' >> /etc/profile.d/crow.sh  
RUN echo 'export PATH=/OpenBLAS/bin:/openmpi/bin:/usr/local/cuda/bin:$PATH' >>
/etc/profile.d/crow.sh  
RUN echo 'export
LD_LIBRARY_PATH="/OpenBLAS/lib:/openmpi/lib:$LD_LIBRARY_PATH"' >>
/etc/profile.d/crow.sh  
RUN echo 'export CUDA_ROOT=/usr/local/cuda' >> /etc/profile.d/crow.sh  
  
USER ${USERNAME}  
  
ENV SSHDIR ${HOME}/.ssh/  
RUN mkdir -p ${SSHDIR}  
  
# Prepare virtual environment and install crow  
WORKDIR ${HOME}  
RUN mkdir data cache results  
RUN virtualenv -p python --system-site-packages venv  
RUN echo 'cd ${HOME}' >> .profile  
RUN echo '. /etc/profile.d/crow.sh' >> .profile  
RUN echo '. ${HOME}/venv/bin/activate' >> .profile  
  
RUN git clone https://github.com/acopar/crow src  
RUN mv src/.git* . && mv src/* .  
RUN bash -c "source ~/venv/bin/activate && cd crow && python setup.py install"  
  
USER root  
WORKDIR /  
# prepare first run for cuda-cffi  
RUN echo "from cuda_cffi import cusparse" >> build_cusparse.py  
  
COPY start.sh start.sh  
COPY users.sh users.sh  
  
EXPOSE 22  
CMD ["/start.sh"]  

