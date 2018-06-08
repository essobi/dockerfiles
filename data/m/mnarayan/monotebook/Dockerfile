FROM jupyter/scipy-notebook  
  
USER root  
  
# Install latest stable octave version  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
software-properties-common \  
python-software-properties && \  
add-apt-repository ppa:octave/stable && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
libgraphicsmagick++1-dev \  
libhdf5-serial-dev \  
octave=4.2.1 liboctave-dev \  
octave-general octave-struct octave-control octave-image octave-signal \  
octave-statistics octave-communications octave-parallel \  
gnuplot-x11 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
RUN pip install octave_kernel && \  
rm -rf .cache/pip  
  
USER root  
  
#RUN python -m octave_kernel.install  
RUN conda install -c conda-forge oct2py  
  
USER $NB_USER  

