# Set the base image to Ubuntu  
FROM continuumio/miniconda3  
  
# File Author / Maintainer  
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"  
RUN conda install -y pandas=0.19.1 requests=2.11.1 matplotlib=1.5.3 qgrid
ipython-notebook=4.0.4  
  
# use this folder to map against local books and files  
RUN mkdir jupyter  
  
ADD config.py /notebooks/config.py  
WORKDIR /notebooks  
  
# create the default profile for ipython  
RUN ipython profile create  
  
RUN jupyter nbextension enable \--py --sys-prefix widgetsnbextension  
  
# Import this to run construct the font-cache  
RUN python -c "from matplotlib.font_manager import FontManager"  
# ***** Install RISE  
ADD ./RISE-3.x /notebooks/RISE-3.x  
RUN python /notebooks/RISE-3.x/setup.py install  
RUN rm -rf /notebooks/RISE-3.x  
  
EXPOSE 9999  
  
CMD jupyter-notebook \--config=/notebooks/config.py

