#This runs Jupyter datascience-notebook with extra packages installed  
FROM jupyter/minimal-notebook  
MAINTAINER Ian Dahlke <ian.dahlke@gmail.com>  
  
# Install desired packages from scipy-notebook  
RUN pip install \  
pandas \  
matplotlib \  
scipy \  
seaborn \  
scikit-learn \  
scikit-image \  
sympy \  
bokeh  
  
# Add live slideshows with RISE  
RUN pip install RISE && \  
jupyter-nbextension install rise --py --sys-prefix && \  
jupyter-nbextension enable rise --py --sys-prefix  
  
# Add ipyleaflet plugin for Jupyter  
RUN pip install ipyleaflet && \  
jupyter nbextension install --py --sys-prefix ipyleaflet && \  
jupyter nbextension enable \--py --sys-prefix ipyleaflet  
  
# Add Octave and Octave kernel  
USER root  
RUN apt-get -yq update && apt-get -yq install octave && apt-get clean  
USER jovyan  
RUN pip install octave_kernel  
  
# Add bash kernel  
RUN pip install bash_kernel && \  
python -m bash_kernel.install  
  
# set auth token to null string. i.e. disable auth.  
RUN mkdir ~/.jupyter && \  
echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py  
  
# set up brew package manager  
USER root  
RUN apt-get -yq update && apt-get install -yq \  
build-essential \  
curl \  
file \  
git \  
python-setuptools \  
&& apt-get clean  
USER jovyan  
  
RUN mkdir ~/.linuxbrew \  
&& git clone https://github.com/Linuxbrew/brew.git ~/.linuxbrew  
ENV PATH="$HOME/.linuxbrew/bin:${PATH}"  
ENV MANPATH="$(brew --prefix)/share/man:${MANPATH}"  
ENV INFOPATH="$(brew --prefix)/share/info:${INFOPATH}"  
# install Humor-Sans.ttf for xkcd plots  
USER root  
RUN apt-get update -yq && apt-get install -yq fonts-humor-sans  
USER jovyan  

