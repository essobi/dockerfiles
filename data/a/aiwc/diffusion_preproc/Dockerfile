# Docker file for the diffusion_preproc plugin app  
FROM fnndsc/ubuntu-python3:latest  
MAINTAINER fnndsc "dev@babymri.org"  
ENV APPROOT="/usr/src/diffusion_preproc" VERSION="0.1"  
COPY ["diffusion_preproc", "${APPROOT}"]  
COPY ["requirements.txt", "${APPROOT}"]  
  
WORKDIR $APPROOT  
  
RUN pip install -r requirements.txt  
  
CMD ["diffusion_preproc.py", "--json"]  
  
# Create a base docker container that can execute FSL commands  
#  
# Example usage:  
# docker run --rm -ti \  
# vistalab/fsl-v5.0 <fsl_command> <input_arguments>  
#  
# Start with neurodebian image  
#FROM neurodebian:trusty  
# Run apt-get calls  
RUN apt-get update  
RUN apt-get install -y wget  
RUN wget -O- http://neuro.debian.net/lists/xenial.us-nh.full | tee
/etc/apt/sources.list.d/neurodebian.sources.list  
RUN apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80
0xA5D32F012649A5A9  
RUN apt-get update  
  
#COPY sources /etc/apt/sources.list.d/neurodebian.sources.list  
RUN apt-get update && apt-get install -y fsl-5.0-core  
  
# Configure environment  
ENV FSLDIR=/usr/lib/fsl/5.0  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
ENV PATH=$PATH:$FSLDIR  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$FSLDIR  
  
# Run configuration script for normal usage  
RUN echo ". /etc/fsl/5.0/fsl.sh" >> /root/.bashrc  
  

