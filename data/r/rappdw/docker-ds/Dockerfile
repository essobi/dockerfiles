######  
#  
# Use Multi-stage build to cut down on size and layers of final image (this
saves about 2GB)  
# with some complications to the build file.  
#  
# Install jupyter and extensions into the builder image and then update
permissions  
# then copy things into the final image.  
#  
# This requires that we do much of what is done in nvidia-python in this
docker file as  
# well. Not idea, but the space savings is worth it.  
#  
######  
  
FROM rappdw/nvidia-python-node as builder  
  
COPY root/ /  
  
RUN pip install -r /tmp/requirements.txt  
  
RUN jupyter serverextension enable --py jupyterlab \  
&& jupyter nbextension enable --py widgetsnbextension \  
&& jupyter labextension install \  
@jupyter-widgets/jupyterlab-manager \  
jupyter-matplotlib \  
jupyterlab_bokeh \  
@pyviz/jupyterlab_pyviz \  
@jupyterlab/plotly-extension  
  
RUN fix-permissions $HOME /.cpu-env /.gpu-env /usr/local/lib /usr/local/share
/usr/local/bin \  
&& mkdir /.cpu-env/share \  
&& cp -r /usr/local/share/jupyter /.cpu-env/share \  
&& cp /usr/local/bin/jupyter* /.cpu-env/bin \  
&& mkdir /.gpu-env/share \  
&& cp -r /usr/local/share/jupyter /.gpu-env/share \  
&& cp /usr/local/bin/jupyter* /.gpu-env/bin  
  
FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04  
ARG DEBIAN_FRONTEND=noninteractive  
LABEL maintainer="rappdw@gmail.com"  
ENV PYTHON_VERSION=3.6.5 \  
PYTHON_PIP_VERSION=9.0.3 \  
NODE_VERSION=8.10.0 \  
YARN_VERSION=1.5.1  
  
RUN chmod 1777 /tmp \  
&& apt-get update && apt-get install --no-install-recommends --allow-
unauthenticated -y \  
build-essential \  
bzip2 \  
ca-certificates \  
curl \  
git \  
gfortran \  
graphviz \  
libatlas-base-dev \  
libblas-common \  
libblas3 \  
libblas-dev \  
libffi-dev \  
libfreetype6 \  
libfreetype6-dev \  
libjpeg8 \  
libjpeg8-dev \  
liblapack-dev \  
libreadline6 \  
libreadline6-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
locales \  
openssl \  
pkg-config \  
sudo \  
vim \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen  
  
# Configure environment  
ENV SHELL=/bin/bash \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
HOME=/home/jovyan  
  
# assumes that the project has been mounted into /home/jovyan/project  
# to ensure this derived projects should add the following to their
dockerutils.cfg file  
# [notebook]  
# volumes=--mount type=bind,source={project_root},target=/home/jovyan/project  
  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER  
  
COPY --from=builder /usr/local /usr/local  
COPY --from=builder /.cpu-env /.cpu-env  
COPY --from=builder /.gpu-env /.gpu-env  
COPY --from=builder /docker-entrypoint.sh /  
COPY root/etc/jupyter/jupyter_notebook_config.py /etc/jupyter/  
# setup useful links and install some dependencies for python  
RUN ln -s /.cpu-env/bin/activate /cpu-env \  
&& ln -s /.gpu-env/bin/activate /gpu-env \  
&& ldconfig \  
&& cd /usr/local/bin \  
&& rm idle pydoc python python-config \  
&& ln -Fs idle3 idle \  
&& ln -Fs pydoc3 pydoc \  
&& ln -Fs python3 python \  
&& ln -Fs python3-config python-config \  
&& apt-get update && apt-get install -y --no-install-recommends \  
tcl \  
tk \  
libffi-dev \  
libgomp1 \  
libssl-dev \  
&& apt-get clean \  
&& rm -rf /var/tmp /tmp /var/lib/apt/lists/* \  
&& mkdir -p /var/tmp /tmp  
  
RUN chmod a+rwX /usr/local/bin  
  
EXPOSE 8888  
WORKDIR $HOME  
ENV WORKDIR=$HOME/project  
USER $NB_USER  
CMD ["start-notebook.sh"]  
ENTRYPOINT ["/docker-entrypoint.sh"]  

