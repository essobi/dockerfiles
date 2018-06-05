FROM meteorhacks/meteord:onbuild  
# Install miniconda to /miniconda  
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-
Linux-x86_64.sh  
RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b  
RUN rm Miniconda-latest-Linux-x86_64.sh  
ENV PATH=/miniconda/bin:${PATH}  
RUN conda update -y conda  
  
RUN conda install -y numpy  
RUN conda install -y pandas  
RUN conda install -c https://conda.anaconda.org/auto colormath  
RUN conda install -y scikit-learn

