# This is the Dockerfile to create the docker image for the workshop in
Frankfurt  
#  
# For the python and nipype part of the workshop use the following command:  
# docker run -it --rm -p 8888:8888 miykael/workshop_frankfurt  
FROM miykael/nipype_tutorial:latest  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
  
# Install software for MNE  
RUN apt-get update -qq \  
&& apt-get install -y -q --no-install-recommends \  
gcc \  
libc-dev \  
libglu1-mesa \  
libgl1-mesa-glx \  
libxt6 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER neuro  
  
#---------------------------------------  
# Install MNE in the 'neuro' environment  
#---------------------------------------  
RUN bash -c 'curl -L https://raw.githubusercontent.com/mne-tools/mne-
python/master/environment.yml -o /opt/miniconda-latest/environment.yml'  
RUN conda env create -q --name mne --file /opt/miniconda-
latest/environment.yml \  
&& rm -f /opt/miniconda-latest/environment.yml  
  
#------------------------------------------------------------  
# Update conda environment 'neuro' for visualization examples  
#------------------------------------------------------------  
# Install missing python software  
RUN bash -c "source activate neuro \  
&& conda install -y -q bokeh \  
holoviews \  
nilearn \  
plotly \  
scikit-image \  
scipy=0.19" \  
&& conda clean -tipsy  
  
USER root  
  
# Install software for PyMVPA  
RUN apt-get update -qq \  
&& apt-get install -y -q --no-install-recommends swig \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER neuro  
RUN bash -c "source activate neuro \  
&& pip install --upgrade pip pymvpa2"  
  
USER root  
  
# Install workshop notebooks and slides  
COPY [".", "/home/neuro/workshop"]  
RUN chown -R neuro /home/neuro/workshop  
RUN rm -rf /opt/miniconda-latest/pkgs/*  
  
USER neuro  
  
RUN mkdir -p ~/.jupyter && echo c.NotebookApp.ip = \"0.0.0.0\" >
~/.jupyter/jupyter_notebook_config.py  
WORKDIR /home/neuro  
  
CMD ["jupyter-notebook"]  

