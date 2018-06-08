# PSI4 Dockerfile  
#  
# credits to:  
#  
# https://github.com/cgsanchez/ScienceContainers/Psi4  
  
FROM continuumio/miniconda3:4.4.10  
  
MAINTAINER A. Zonca <zonca@sdsc.edu>  
  
# Also Prune MKL to reduce image size  
# add first the psi4 channel and then the psi4/agg channel, so that the second
has higher priority  
  
RUN conda install --yes psi4 -c psi4/label/agg -c psi4 && \  
conda clean -tipsy && \  
cd /opt/conda/lib && \  
mkdir tmp && \  
mv *mkl* tmp/ && \  
cd tmp && \  
mv libmkl_core.so libmkl_intel_lp64.so libmkl_intel_thread.so libmkl_mc3.so
libmkl_rt.so /opt/conda/lib/ && \  
rm -r /opt/conda/lib/tmp/ && \  
cd /opt/conda/pkgs/mkl-*/lib && \  
mkdir tmp && \  
mv *mkl* tmp/ && \  
cd tmp && \  
mv libmkl_core.so libmkl_intel_lp64.so libmkl_intel_thread.so libmkl_mc3.so
libmkl_rt.so .. && \  
cd .. && \  
rm -r tmp/  
  
#  
# The scratch_dir should be used for scratch files, mounted at runtime  
# The run_dir would contain the input and output files, mounted at runtime  
#  
#VOLUME /scratch_dir  
#VOLUME /run_dir  
#  
# Set one thread by default, can be overriden at runtime  
#  
ENV MKL_NUM_THREADS=1  
ENV OMP_NUM_THREADS=1  
#  
# Point scratch space to mounted scratch directory  
#  
#ENV PSI_SCRATCH=/scratch_dir  
#WORKDIR /run_dir  
RUN mkdir -p /root/shared/results  
  
COPY psi4_test.py run_psi4.py /  

