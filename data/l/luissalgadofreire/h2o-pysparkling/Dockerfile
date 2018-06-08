# Dockerfile based on jupyter/all-spark-notebook.  
# See: https://github.com/jupyter/docker-stacks/tree/master/all-spark-notebook  
FROM jupyter/all-spark-notebook  
  
MAINTAINER luissalgadofreire  
  
ENV MASTER "local[*]"  
USER root  
  
# Install all OS dependencies for openai gym  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
python-numpy \  
python-dev \  
cmake \  
zlib1g-dev \  
libjpeg-dev \  
xvfb \  
libav-tools \  
xorg-dev \  
python-opengl \  
libboost-all-dev \  
libsdl2-dev \  
swig \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install ffmpeg for video handling  
RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -yq --no-install-recommends ffmpeg  
  
# Switch back to jovyan to avoid accidental container running as root  
USER $NB_USER  
  
# Add channels to conda to install custom packages  
RUN conda config --add channels menpo # for opencv  
  
# Set the working directory  
WORKDIR /home/$NB_USER/work  
  
# Install binary packages with conda from requirements-conda.txt.  
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to  
# use notebook-friendly backends in these images  
ONBUILD COPY requirements-conda.txt /home/jovyan/work  
ONBUILD RUN conda install --quiet --yes --file requirements-conda.txt && \  
conda remove --quiet --yes --force qt pyqt && \  
conda clean -tipsy  
  
# Install python packages with pip from requirements-pip.txt  
ONBUILD COPY requirements-pip.txt /home/jovyan/work  
ONBUILD RUN pip install --no-cache-dir -r requirements-pip.txt  
  
# Deploy application code  
ONBUILD COPY . /home/$NB_USER/work  
  
# Install H2O pysparkling requirements  
RUN pip install requests && \  
pip install tabulate && \  
pip install six && \  
pip install future && \  
pip install colorama  
  
# Expose H2O Flow UI ports  
EXPOSE 54321  
EXPOSE 54322  
EXPOSE 55555  
# Install H2O sparkling water  
RUN \  
cd /home/$NB_USER && \  
wget http://h2o-release.s3.amazonaws.com/sparkling-water/rel-2.1/7/sparkling-
water-2.1.7.zip && \  
unzip sparkling-water-2.1.7.zip && \  
cd sparkling-water-2.1.7  
  
# Add sparkling-water's /bin folder to path  
ENV PATH="/home/$NB_USER/sparkling-water-2.1.7/bin:${PATH}"  
# Switch back to jovyan to avoid container running accidentally as root  
USER $NB_USER  

