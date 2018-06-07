FROM neurodebian:latest  
MAINTAINER Joke Durnez  
  
# Preparations  
RUN ln -snf /bin/bash /bin/sh  
ENV SHELL /bin/bash  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Update packages and install the minimal set of tools  
RUN sed -i -e 's,main$,main contrib non-free,g'
/etc/apt/sources.list.d/neurodebian.sources.list && \  
apt-get -y update && \  
apt-get install -y curl \  
git \  
xvfb \  
bzip2 \  
apt-utils \  
tcsh \  
bc \  
tar \  
libgomp1 \  
perl-modules \  
fsl-core \  
afni \  
graphviz && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Set FSL environment variables  
ENV FSLDIR=/usr/share/fsl/5.0 \  
FSLOUTPUTTYPE=NIFTI_GZ \  
FSLMULTIFILEQUIT=TRUE \  
POSSUMDIR=/usr/share/fsl/5.0 \  
FSLTCLSH=/usr/bin/tclsh \  
FSLWISH=/usr/bin/wish \  
PATH=/usr/lib/fsl/5.0:$PATH \  
LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH  
  
# Install ANTs  
RUN mkdir -p /opt/ants && \  
curl -sSL
"https://files.osf.io/v1/resources/fvuh8/providers/osfstorage/57f34767594d9001ef91bfb7"
\  
| tar -xjC /opt/ants --strip-components 1  
ENV ANTSPATH /opt/ants  
ENV PATH $ANTSPATH:$PATH  
  
# Install BIDS-validator  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
npm install -g bids-validator  
  
# Install C3D  
RUN mkdir -p /opt/c3d && \  
curl -sSL
"https://files.osf.io/v1/resources/fvuh8/providers/osfstorage/57f341d6594d9001f591bac2"
\  
| tar -xzC /opt/c3d --strip-components 1  
  
ENV C3DPATH=/opt/c3d  
ENV
PATH=$C3DPATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH  
  
# Install debian dependencies of python packages  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && \  
apt-get install -y graphviz \  
pandoc &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
  
# Install miniconda  
RUN curl -sSLO https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh && \  
/bin/bash Miniconda2-latest-Linux-x86_64.sh -b -p /usr/local/miniconda && \  
rm Miniconda2-latest-Linux-x86_64.sh  
  
ENV PATH /usr/local/miniconda/bin:$PATH  
ENV PATH /usr/lib/afni/bin:$PATH  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# Create conda environment, use nipype's conda-forge channel  
RUN conda config --add channels conda-forge && \  
conda install -y lockfile nipype matplotlib  
  
# Install pip  
RUN pip install --upgrade pip && \  
pip install psutil && \  
pip install sklearn && \  
pip install nilearn && \  
pip install pandas && \  
pip install statsmodels && \  
python -c "from matplotlib import font_manager"  
  
CMD ["/bin/bash"]  

