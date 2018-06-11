FROM python:2.7  
MAINTAINER Jordan Li <twistedogic@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get install -y build-essential gfortran g++ libopenblas-dev git wget
libxrender1 libfontconfig1 libsm6 libglib2.0-0 libfreetype6 unzip  
RUN wget --quiet http://repo.continuum.io/miniconda/Miniconda-latest-
Linux-x86_64.sh && \  
bash Miniconda-latest-Linux-x86_64.sh -b -p /opt/miniconda && \  
rm Miniconda-latest-Linux-x86_64.sh  
ENV PATH /opt/miniconda/bin:$PATH  
RUN chmod -R a+rx /opt/miniconda  
  
# Install PyData modules and IPython dependencies  
RUN conda update --quiet --yes conda && \  
conda install --quiet --yes numpy scipy pandas matplotlib cython pyzmq scikit-
learn seaborn six statsmodels pip tornado jinja2 sphinx pygments nose readline
sqlalchemy  
  
# Set up IPython kernel  
RUN pip install graphlab-create==1.3  
RUN pip install ipython  
RUN pip install tornado --upgrade  
RUN pip install jsonschema  
RUN pip install jsonpointer  
RUN pip install terminado  
RUN python -c "import numpy, scipy, pandas, matplotlib, matplotlib.pyplot,
sklearn, seaborn, statsmodels, graphlab"  
RUN (mkdir -p ~/.graphlab && echo "[Product]\nproduct_key=<key>" >
~/.graphlab/config && echo "Configuration file written") || echo
"Configuration file not written"  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/opt/miniconda/lib  
ADD start.sh /start.sh  
RUN chmod u+x /start.sh  
  
# Add java  
RUN apt-get install -y openjdk-7-jre  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV GRAPHLAB_JAVA__HOME /usr/lib/jvm/java-7-openjdk-amd64  
VOLUME /notebooks  
WORKDIR /notebooks  
CMD /start.sh  

