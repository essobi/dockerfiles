# docker build -t gromacs .  
  
FROM lipcomputing/nvidia-ubuntu16.04:nvdrv_375.26  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Run Gromacs with CUDA enabled"  
  
RUN ansible-galaxy install git+https://github.com/LIP-Computing/ansible-role-
gromacs.git && \  
ansible-playbook /etc/ansible/roles/ansible-role-gromacs/tests/gromacs.yml  
  
RUN apt-get install -y strace  
  
ENV GROMACS_DIR /usr/local/gromacs  
ENV GMXBIN $GROMACS_DIR/bin  
ENV GMXDATA $GROMACS_DIR/share/gromacs  
ENV GMXLDLIB $GROMACS_DIR/lib  
ENV GMXMAN $GROMACS_DIR/share/man  
  
ENV PATH $GMXBIN:/usr/local/cuda-8.0/bin:$PATH  
ENV LD_LIBRARY_PATH $GMXLDLIB:/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH  
ENV MANPATH $GMXMAN:$MANPATH  
ENV PKG_CONFIG_PATH $GMXLDLIB/pkgconfig:$PKG_CONFIG_PATH  

