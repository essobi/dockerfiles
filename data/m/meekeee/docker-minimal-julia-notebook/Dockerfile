# First test by Michele Giugliano at Julia Jupyter Minimal Notebook  
# Distributed under the terms of the Modified BSD License.  
# Compiled invoking: docker build -t minimal-julia-notebook .  
FROM jupyter/minimal-notebook  
  
USER root  
  
ENV JULIA_DIR /opt/julia  
ENV PATH $JULIA_DIR/bin:$PATH  
  
# Install matplotlib as jovyan  
RUN mkdir -p /opt/julia && \  
chown jovyan /opt/julia  
  
USER jovyan  
  
# Install matplotlib as jovyan  
RUN conda install --quiet --yes matplotlib ipywidgets  
#ipywidgets=4.1.1  
# Install Julia as jovyan  
RUN cd /tmp && \  
wget --quiet
https://julialang.s3.amazonaws.com/bin/linux/x64/0.4/julia-0.4.5-linux-x86_64.tar.gz
&& \  
tar -xzf julia-0.4.5-linux-x86_64.tar.gz && \  
mv /tmp/julia*/* /opt/julia/ && \  
rm julia-0.4.5-linux-x86_64.tar.gz  
  
# Configure Julia and add packages  
COPY julia_init.jl /tmp/  
  
RUN /opt/julia/bin/julia /tmp/julia_init.jl  
  
RUN jupyter nbextension enable \--py widgetsnbextension  
  

