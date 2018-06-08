FROM jupyter/scipy-notebook  
  
USER root  
  
# Install octave and gnuplot  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
octave \  
octave-control octave-image octave-io octave-optim octave-signal octave-
statistics \  
gnuplot && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
RUN pip install octave_kernel && \  
rm -rf .cache/pip  
  
USER root  
  
RUN python -m octave_kernel.install  
  
USER $NB_USER  
  
VOLUME /home/$NB_USER/work  

