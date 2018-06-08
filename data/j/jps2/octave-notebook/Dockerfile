FROM jupyter/minimal-notebook  
  
USER root  
  
RUN apt-get update  
RUN apt-get install octave -y  
  
RUN pip install octave_kernel  
RUN python -m octave_kernel.install  

