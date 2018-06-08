FROM jupyter/minimal-notebook:latest  
MAINTAINER Kacper Kowalik <xarthisius.kk@gmail.com>  
RUN pip install numpy!=1.14.0 ytree  
RUN ipython -c 'from matplotlib.font_manager import FontManager;
FontManager()'  
WORKDIR /home/jovyan/work  

