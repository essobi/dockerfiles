FROM twistedogic/spark-mesos  
MAINTAINER Jordan Li  
RUN apt-get update -y  
RUN apt-get install -y build-essential gfortran g++ libopenblas-dev git wget
libxrender1 libfontconfig1 libsm6 libglib2.0-0 libfreetype6 unzip python2.7  
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
  
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz &&
\  
tar -xvzf ta-lib-0.4.0-src.tar.gz && \  
cd ta-lib/ && \  
./configure --prefix=/usr && \  
make && \  
make install  
# Python wrapper  
RUN git clone https://github.com/mrjbq7/ta-lib.git /ta-lib-py && cd ta-lib-py
&& python setup.py install  
  
ENV SPARK_HOME /opt/spark/  
  
RUN ipython profile create pyspark  
  
ADD ipython_notebook_config.py
/.ipython/profile_pyspark/ipython_notebook_config.py  
ADD 00-pyspark-setup.py /.ipython/profile_pyspark/startup/00-pyspark-setup.py  
ADD supervisord.conf /etc/supervisord.conf  

