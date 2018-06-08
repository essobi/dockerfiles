#  
# Dockerfile for "neurojupyter" container  
#  
# See https://groups.google.com/forum/#!topic/neuralensemble/4btzM0n_9O4  
# and the excellent guidance by Andrew Davison (andrew.davison@unic.cnrs-
gif.fr).  
#  
# Build it by:  
# docker build -t neurojupyter .  
#  
# Jan 27th 2018, Michele GIUGLIANO (michele.giugliano@uantwerpen.be)  
#  
#FROM neuralensemble/simulation:py2  
FROM neuralensemble/simulation:py3_pynn092  
MAINTAINER michele.giugliano@uantwerpen.be  
  
USER docker  
RUN /home/docker/env/neurosci/bin/pip install jupyter  
RUN /home/docker/env/neurosci/bin/pip install jupyterlab  
RUN /home/docker/env/neurosci/bin/jupyter serverextension enable \--py
jupyterlab --sys-prefix  
RUN /home/docker/env/neurosci/bin/pip install ipywidgets  
RUN /home/docker/env/neurosci/bin/jupyter nbextension enable \--py
widgetsnbextension  
  
USER root  
  
ENV JULIA_PATH /home/docker/env/neurosci/julia  
ENV JULIA_VERSION 0.6.2  
RUN mkdir $JULIA_PATH \  
&& apt-get update && apt-get install -y curl && apt-get install -y libzmq3\  
&& curl -sSL
"https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"
-o julia.tar.gz \  
&& tar -xzf julia.tar.gz -C $JULIA_PATH \--strip-components 1 \  
&& rm -rf julia.tar.gz*  
ENV PATH $JULIA_PATH/bin:$PATH  
  
COPY julia_init.jl /tmp/  
#COPY julia_start.jl /tmp/  
RUN julia /tmp/julia_init.jl  
  
ENV TINI_VERSION v0.6.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
EXPOSE 8888  
VOLUME /opt/notebooks  
WORKDIR /opt/notebooks  
  
CMD ["/home/docker/env/neurosci/bin/jupyter", "lab", "--port=8888", "--no-
browser", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--
notebook-dir=/opt/notebooks"]  

