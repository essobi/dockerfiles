FROM jupyter/base-notebook  
  
MAINTAINER Pan Luo <pan.luo@ubc.ca>  
  
ENV GOOGLE_APPLICATION_CREDENTIALS /home/jovyan/work/google.json  
  
USER root  
  
# Install all OS dependencies for fully functional notebook server  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
build-essential \  
git \  
python-dev \  
unzip \  
libsm6 \  
pandoc \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN conda install --quiet --yes \  
'matplotlib=2.0*' \  
#'pandas-gbq' \  
'plotly=2.0.*' \  
'google-api-python-client=1.6.*' && \  
conda clean -tipsy  
  
RUN pip install git+git://github.com/xcompass/pandas-gbq@master  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_USER  
  
ADD . /home/jovyan/work  
WORKDIR /home/jovyan/work  

