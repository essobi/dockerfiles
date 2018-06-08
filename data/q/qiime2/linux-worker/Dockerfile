# Use tini as PID 1 to handle signals safely  
FROM krallin/ubuntu-tini:xenial  
  
# Locale for click  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
# Utilities  
RUN apt-get update -q  
RUN apt-get install -yq wget unzip bzip2 git build-essential  
  
# Install conda  
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O /tmp/miniconda3.sh  
RUN /bin/bash /tmp/miniconda3.sh -bp /opt/miniconda3  
RUN rm /tmp/miniconda3.sh  
  
# Update conda and install conda-build  
RUN /opt/miniconda3/bin/conda update -yq conda  
RUN /opt/miniconda3/bin/conda install -yq conda-build  
  
# Set conda environment  
RUN echo "export PATH=/opt/miniconda3/bin:$PATH" > /etc/profile  
ENV PATH /opt/miniconda3/bin:$PATH  

