FROM jupyter/minimal-notebook  
MAINTAINER "Christian Diener <mail [at] cdiener.com>"  
USER root  
RUN apt-get update -y && apt-get install -y wget libgmp-dev unzip && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
USER jovyan  
  
RUN conda update -yq --all && conda install -yq \  
Cython ipython biopython sympy numpy scipy nomkl pandas pytz && \  
pip install python-libsbml "cobra<=0.5.11" escher  
  
# Build solplex extension  
ENV SOPLEX_VERSION="3.0.0"  
COPY soplex-$SOPLEX_VERSION.tgz /tmp  
# Get soplex python extension  
RUN cd /tmp && \  
wget https://github.com/SBRG/soplex_cython/archive/master.zip && \  
unzip master.zip && mv soplex_cython-master soplex_cython  
# Compile patched soplex  
RUN cd /tmp && \  
tar xvzf soplex-$SOPLEX_VERSION.tgz && mv soplex-$SOPLEX_VERSION soplex && \  
cd soplex/src && patch -b < /tmp/soplex_cython/long-double.patch && cd .. && \  
USRCPPFLAGS=" -DWITH_LONG_DOUBLE " make SHARED=true GMP=true ZLIB=false
VERBOSE=true  
# Build soplex python extension  
RUN cd /tmp/soplex && ar crs libsoplex.a obj/*/lib/* && \  
mv libsoplex.a /tmp/soplex_cython && cd /tmp/soplex_cython && pip install .  
  
# Install cobrame and ECOLIme  
RUN pip install https://github.com/SBRG/cobrame/archive/master.zip \  
https://github.com/SBRG/ecolime/archive/master.zip  
# Add example notebooks  
RUN cd /home/jovyan/work && wget \  
https://github.com/SBRG/ecolime/raw/master/ecolime/build_ME_model.ipynb && \  
ln -s /opt/conda/lib/python3.5/site-packages/ecolime/build_ME_model.py  
  
# Copy examples and clean up  
RUN conda clean -tipsy  
USER root  
COPY getting_started.ipynb /home/jovyan/work  
RUN mkdir /home/jovyan/work/me_models  
COPY iLE1678.pickle /home/jovyan/work/me_models  
RUN chown -R jovyan:users /home/jovyan/work/*  
RUN rm -rf /tmp/*  
USER jovyan  

