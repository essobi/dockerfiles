# its_docker_ngf  
FROM continuumio/miniconda3:4.3.14  
ARG DEBIAN_FRONTEND=noninteractive  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
WORKDIR /code  
COPY environment.yml /code  
  
# Create conda env  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends build-essential \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& conda env create -f /code/environment.yml -n heathcliff \  
&& conda clean -tipsy \  
&& mkdir -p /var/log/app && mkdir /logs  
  
ENV PATH="/opt/conda/envs/heathcliff/bin:$PATH" \  
CONDA_DEFAULT_ENV="heathcliff" \  
CONDA_PREFIX="/opt/conda/envs/heathcliff" \  
GDAL_DATA="/opt/conda/envs/heathcliff/share/gdal" \  
CPL_ZIP_ENCODING="UTF-8" \  
PROJ_LIB="/opt/conda/envs/heathcliff/share/proj"  
# RUN mkdir -p /var/log/app && mkdir /logs  
COPY . /code/  

