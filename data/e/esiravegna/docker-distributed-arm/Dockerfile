FROM resin/armv7hf-debian  
MAINTAINER Esteban Siravegna <esiravegna@gmail.com>  
RUN [ "cross-build-start" ]  
  
RUN apt-get update -yqq && apt-get install -yqq \  
wget \  
bzip2 \  
git \  
libglib2.0-0 \  
libfreetype6-dev \  
  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure environment  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
# Folder to install non-system tools and serve as workspace for the notebook  
# user  
RUN mkdir -p /work/bin  
  
# Create a non-priviledge user that will run the services  
#ENV BASICUSER basicuser  
#ENV BASICUSER_UID 1000  
#RUN useradd -m -d /work -s /bin/bash -N -u $BASICUSER_UID $BASICUSER  
#RUN chown $BASICUSER /work  
#USER $BASICUSER  
# Deactivate basic user to make it easier to deal with volume permissions  
# for now  
ENV BASICUSER root  
WORKDIR /work  
  
# Install Python 3 from miniconda  
RUN wget -O miniconda.sh \  
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh \  
&& bash miniconda.sh -b -p /work/miniconda \  
&& rm miniconda.sh  
  
ENV PATH="/work/bin:/work/miniconda/bin:$PATH"  
# Install matplotlib and scikit-image without Qt  
RUN conda update -y python conda && \  
conda install -y python=3.6 -c rpi && \  
conda install -y --no-deps -c rpi \  
freetype \  
cycler \  
libpng \  
pyparsing \  
pytz \  
python-dateutil \  
networkx \  
pillow \  
six \  
#&& conda install -y --no-deps -c jamalsenouci statsmodels \  
&& conda clean -tipsy  
  
RUN conda install -y -c rpi \  
pip \  
setuptools \  
notebook \  
terminado \  
psutil \  
numpy \  
scipy \  
pandas \  
bokeh \  
matplotlib \  
scikit-image \  
scikit-learn \  
&& conda clean -tipsy  
  
# Install the master branch of distributed and dask  
COPY requirements.txt .  
RUN pip install -r requirements.txt && rm -rf ~/.cache/pip/  
  
# Add local files at the end of the Dockerfule to limit cache busting  
COPY start-notebook.sh ./bin/  
COPY start-dworker.sh ./bin/  
COPY start-dscheduler.sh ./bin/  
COPY examples examples  
  
# Configure matplotlib to avoid using QT  
COPY matplotlibrc /work/.config/matplotlib/matplotlibrc  
  
# Trigger creation of the matplotlib font cache  
ENV MATPLOTLIBRC /work/.config/matplotlib  
RUN python -c "import matplotlib.pyplot"  
  
# Switch back to root to make it possible to do interactive admin/debug as  
# root tasks with docker exec  
USER root  
# Files added via COPY need a manual chown  
RUN chown $BASICUSER:users -R /work/.config /work/examples /work/bin
/work/requirements.txt  
  
# Install Tini that necessary to properly run the notebook service in a docker  
# container:  
# http://jupyter-notebook.readthedocs.org/en/latest/public_server.html#docker-
cmd  
RUN [ "cross-build-end" ]  
CMD [ "/bin/bash" ]  

