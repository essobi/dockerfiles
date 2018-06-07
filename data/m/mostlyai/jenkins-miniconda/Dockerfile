FROM jenkins/jenkins:lts  
  
LABEL maintainer="ci@mostly.ai"  
  
USER root  
  
ARG CONDA_DIR="/opt/conda"  
# Install Miniconda  
RUN mkdir /tmp/miniconda  
WORKDIR /tmp/miniconda  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh  
RUN ./Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR  
  
# Add mostlyai and conda-forge as systemwide channels  
RUN $CONDA_DIR/bin/conda config --add channels conda-forge --system  
RUN $CONDA_DIR/bin/conda config --add channels mostlyai --system  
  
# Change non-interactive shell to bash - Miniconda activate fails for  
# R packages in dash as it doesn't support functions in shell scripts  
RUN echo "dash dash/sh boolean false" | debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash  
  
# Clean up  
WORKDIR /  
RUN rm -rf /tmp/miniconda  
  
USER jenkins  

