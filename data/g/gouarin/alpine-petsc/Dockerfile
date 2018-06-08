FROM gouarin/alpine-base  
  
MAINTAINER Loic Gouarin "loic.gouarin@gmail.com"  
ENV USER=precis  
  
COPY environment.yml environment.yml  
RUN conda env create -f environment.yml &&\  
rm -rf $CONDA_DIR/pkgs  
  
ENV PATH=$CONDA_DIR/envs/$USER/bin:$PATH  
ENV CONDA_ENV_PATH=$CONDA_DIR/envs/$USER  
ENV CONDA_DEFAULT_ENV=$USER  
RUN adduser -s /bin/bash -D $USER  
  
WORKDIR /home/$USER  

