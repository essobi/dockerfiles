# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
RUN apt-get update  
RUN apt-get install -y -q software-properties-common  
  
###############################  
# Install compiler and perl stuff  
RUN apt-get install -y -q libboost-iostreams-dev libboost-system-dev libboost-
filesystem-dev  
RUN apt-get install -y -q zlibc gcc-multilib apt-utils zlib1g-dev python
python-pip  
RUN apt-get install -y -q libx11-dev libxpm-dev libxft-dev libxext-dev
libncurses5-dev  
RUN apt-get install -y -q cmake tcsh build-essential g++ git wget gzip perl
unzip  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y -q vim samtools  
  
###############################  
# GMAP  
RUN wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2015-12-31.v6.tar.gz  
RUN tar zxvf gmap-gsnap-2015-12-31.v6.tar.gz  
RUN cd /gmap-2015-12-31 && ./configure && make && make install  
  
###############################  
# MASH  
RUN wget https://github.com/marbl/Mash/releases/download/v1.0.2/mash-
Linux64-v1.0.2.tar.gz && \  
tar zxvf mash-Linux64-v1.0.2.tar.gz  
RUN mv mash /usr/bin/  
  
###############################  
  
# Force bash always  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
# Default conda installation  
ENV CONDA_ENV_PATH /anaconda3  
ENV MY_CONDA_COGENTENV "anaCogent"  
# This is how you will activate this conda environment  
ENV CONDA_ACTIVATE "source $CONDA_ENV_PATH/bin/activate $MY_CONDA_COGENTENV"  
  
###############################  
# COGENT  
WORKDIR /  
RUN wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh  
RUN bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p $CONDA_ENV_PATH && chmod -R
a+rx $CONDA_ENV_PATH  
ENV PATH=$CONDA_ENV_PATH/bin:$PATH  
RUN conda create -y -n $MY_CONDA_COGENTENV python=2.7 anaconda  
RUN conda update --quiet --yes conda  
RUN conda install -y -n $MY_CONDA_COGENTENV biopython && \  
conda install -y -n $MY_CONDA_COGENTENV -c http://conda.anaconda.org/cgat bx-
python  
RUN conda clean -y -t  
RUN $CONDA_ACTIVATE && pip install --upgrade pip && pip install pulp  
RUN git clone https://github.com/Magdoll/Cogent.git  
RUN $CONDA_ACTIVATE && cd /Cogent && git submodule update --init --recursive
&& cd Complete-Striped-Smith-Waterman-Library/src && make && \  
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Cogent/Complete-Striped-Smith-
Waterman-Library/src && \  
export PYTHONPATH=$PYTHONPATH:/Cogent/Complete-Striped-Smith-Waterman-
Library/src && \  
$CONDA_ACTIVATE && cd /Cogent && python setup.py build && python setup.py
install && cd /  
  
###############################  
# Script: Activate virtualenv and launch cogent  
ENV STARTSCRIPT /opt/start  
RUN echo "#!/bin/bash" > $STARTSCRIPT  
RUN echo "$CONDA_ACTIVATE" >> $STARTSCRIPT  
RUN echo -e "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Cogent/Complete-Striped-
Smith-Waterman-Library/src" >> $STARTSCRIPT  
RUN echo -e "export PYTHONPATH=$PYTHONPATH:/Cogent/Complete-Striped-Smith-
Waterman-Library/src" >> $STARTSCRIPT  
RUN echo -e "run_mash.py --version" >> $STARTSCRIPT  
RUN chmod +x $STARTSCRIPT  
  
###############################  
## How to run  
# docker run -v /yourdatadir:/data --rm -it cogent  
## add your command to /opt/start , for example:  
# echo -e "run_mash.py --version" >> /opt/start  
## run  
# /opt/start  
  
  

