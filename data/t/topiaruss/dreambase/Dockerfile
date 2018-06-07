#FROM topiaruss/nvidia-ub1404cuda80:8.0-devel-cudnn5  
#FROM nvidia/cuda:8.0-cudnn5-devel  
FROM nvidia/cuda:7.5-cudnn5-devel  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && \  
apt-get install -y \  
wget bzip2 ca-certificates \  
libfreeimage3 libfreeimage-dev \  
libglib2.0-0 libxext6 libsm6 libxrender1 git gcc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh  
RUN wget --quiet \  
https://repo.continuum.io/miniconda/Miniconda3-4.1.11-Linux-x86_64.sh \  
-O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
ENV PATH /opt/conda/bin:$PATH  
  
COPY environment.yml /home/  
  
RUN echo 'create conda env, clean' && \  
cd /home && conda env create --name dreamkg_docker --force  
  
# I think conda clean was removing pytest related components.  
# && \  
# conda clean -ay  
# Insert useful scripts, and timestamp the build  
COPY scripts /scripts  
  
RUN echo "gpu base created " > /created_gpubase.txt && \  
date >> /created_gpubase.txt  
  
ENTRYPOINT ["/bin/bash", "-c"]  
CMD ["/scripts/ident.sh"]  

