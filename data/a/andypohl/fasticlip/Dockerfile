FROM continuumio/miniconda  
MAINTAINER Andy Pohl <andy.pohl@wisc.edu>  
  
RUN apt-get update && apt-get install -y build-essential pkg-config zip  
  
ENV CONDA_ENV FAST-iCLIP-062017  
ENV CONDA_ENV_PATH /opt/conda/envs/$CONDA_ENV  
ENV FASTICLIP_PATH $CONDA_ENV_PATH/FAST-iCLIP  
  
COPY fasticlip.conda.yml /root  
  
RUN conda update -y conda \  
&& conda env create -p $CONDA_ENV_PATH -f /root/fasticlip.conda.yml  
  
SHELL ["/bin/bash", "-c"]  
  
RUN source activate $CONDA_ENV \  
&& mkdir -p $CONDA_ENV_PATH/src \  
&& cd $CONDA_ENV_PATH/src \  
&& wget -O bowtie2-2.1.0-linux-x86_64.zip
"https://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip/download" \  
&& unzip bowtie2-2.1.0-linux-x86_64.zip \  
&& cp bowtie2-2.1.0/bowtie2* bowtie2-2.1.0/scripts/* $CONDA_ENV_PATH/bin/ \  
&& wget http://www.biolab.si/iCLIPro/dist/iCLIPro-0.1.1.tar.gz \  
&& tar xfz iCLIPro-0.1.1.tar.gz \  
&& cd iCLIPro-0.1.1/ \  
&& python setup.py install --prefix=$CONDA_ENV_PATH \  
&& cd $CONDA_ENV_PATH/src \  
&& wget http://hannonlab.cshl.edu/fastx_toolkit/libgtextutils-0.6.tar.bz2 \  
&& tar xfj libgtextutils-0.6.tar.bz2 \  
&& cd libgtextutils-0.6/ \  
&& ./configure --prefix=$CONDA_ENV_PATH \  
CFLAGS="-Wno-error=unused-but-set-variable" \  
&& make && make install \  
&& cd $CONDA_ENV_PATH/src \  
&& wget http://hannonlab.cshl.edu/fastx_toolkit/fastx_toolkit-0.0.13.tar.bz2 \  
&& tar xfj fastx_toolkit-0.0.13.tar.bz2 \  
&& cd fastx_toolkit-0.0.13/ \  
&& ./configure --prefix=$CONDA_ENV_PATH \  
PKG_CONFIG_PATH=$CONDA_ENV_PATH/lib/pkgconfig \  
CFLAGS="-include/usr/include/x86_64-linux-gnu/sys/types.h" \  
&& make && make install \  
&& cd $CONDA_ENV_PATH/src \  
&& wget https://github.com/alexdobin/STAR/archive/STAR_2.4.2a.tar.gz \  
&& tar xfz STAR_2.4.2a.tar.gz \  
&& cp STAR-STAR_2.4.2a/bin/Linux_x86_64_static/* $CONDA_ENV_PATH/bin/ \  
&& cd $CONDA_ENV_PATH/src \  
&& rm -rf * \  
&& python -c 'import matplotlib; matplotlib.use("Agg"); import
matplotlib.pyplot as plt;'  
# Finally install FAST-iCLIP itself  
COPY setup.py $FASTICLIP_PATH/  
COPY fasticlip $FASTICLIP_PATH/fasticlip/  
COPY bin $FASTICLIP_PATH/bin/  
  
RUN source activate $CONDA_ENV \  
&& cd $FASTICLIP_PATH \  
&& python setup.py install --prefix=$CONDA_ENV_PATH  
  
# These live on the host:  
VOLUME $FASTICLIP_PATH/rawdata $FASTICLIP_PATH/docs $FASTICLIP_PATH/results  
  
WORKDIR $FASTICLIP_PATH  
CMD /bin/bash  

