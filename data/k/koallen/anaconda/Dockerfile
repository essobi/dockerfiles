FROM nvidia/cuda:7.5-cudnn5-devel  
MAINTAINER Liu Siyuan <SLIU019@e.ntu.edu.sg>  
  
# Set anaconda path  
ENV ANACONDA /opt/anaconda  
ENV PATH $ANACONDA/bin:$PATH  
  
# Download anaconda and install it  
RUN apt-get update && apt-get install -y wget build-essential  
RUN wget http://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh -P
/tmp  
RUN bash /tmp/Anaconda2-4.0.0-Linux-x86_64.sh -b -p $ANACONDA  
RUN rm /tmp/Anaconda2-4.0.0-Linux-x86_64.sh  
  
# Copy the config file into docker  
RUN jupyter notebook --generate-config && ipython profile create  
ADD jupyter_notebook_config.py /root/.jupyter  
ADD matplotlib_init.py /root/.ipython/profile_default/startup  
  
# Add Tini  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Change workdir  
WORKDIR /root/workspace  
  
# Default command is to run a jupyter notebook at 0.0.0.0:8888 in headless
mode  
CMD ["jupyter", "notebook"]  

