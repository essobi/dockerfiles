FROM binstar/linux-64  
MAINTAINER MAINTAINER Birdhouse <wps@dkrz.de>  
LABEL Description="conda build image" Vendor="Birdhouse" Version="0.2.3"  
RUN yum update -y && \  
yum install -y epel-release && \  
yum install -y wget curl gcc-c++ make tar bzip2 unzip patch  
RUN yum install -y libXrender libXext libX11  
RUN useradd binstar  
RUN chown binstar:binstar -R /opt/miniconda  
USER binstar  
WORKDIR /home/binstar  
ENV HOME /home/binstar  
ENV PATH /opt/miniconda/bin:$PATH  
RUN conda update -y conda  
RUN conda config \--set always_yes true && \  
conda config \--set channel_priority true && \  
conda config \--add channels defaults && \  
conda config \--add channels conda-forge && \  
conda config \--add channels birdhouse  
  
RUN conda install conda-build jinja2 psutil anaconda-client anaconda-build
llvm mercurial  
CMD ["bash"]  

