FROM python:3.6  
LABEL maintainer "Martin Marcher <martin@marcher.name>"  
  
RUN curl \--silent \--location -o /Miniconda3-latest-Linux-x86_64.sh
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \  
/bin/bash /Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 && \  
rm -f /Miniconda3-latest-Linux-x86_64.sh && \  
/opt/miniconda3/bin/conda config \--add channels conda-forge && \  
/opt/miniconda3/bin/conda config \--add channels defaults && \  
/opt/miniconda3/bin/conda config \--add channels r && \  
/opt/miniconda3/bin/conda config \--add channels bioconda && \  
/opt/miniconda3/bin/conda install \--yes \--quiet mageck-vispr && \  
/opt/miniconda3/bin/conda clean \--yes \--all && \  
curl \--silent \--location -o /opt/miniconda3/lib/python3.5/site-
packages/vispr/cli.py
https://bitbucket.org/liulab/vispr/raw/750cb89b252af113bd2e696d7f932d0f93a15be7/vispr/cli.py
&& \  
echo All Done  
  
ENTRYPOINT ["/opt/miniconda3/bin/vispr"]  

