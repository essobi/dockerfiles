FROM python:3.6-slim  
MAINTAINER Vishwa <hello@vishwa.be>  
  
# Env's  
ENV DEBIAN_FRONTEND noninteractive  
ENV NB_PASSWORD password  
ENV TINI_VERSION v0.6.0  
# Add sources for ffmpeg  
RUN sed -i "s/jessie main/jessie main contrib non-free/" /etc/apt/sources.list  
RUN echo "deb http://http.debian.net/debian jessie-backports main contrib non-
free" >> /etc/apt/sources.list  
  
# Update & install required base packages  
RUN apt-get -yq update && \  
apt-get install --no-install-recommends -y build-essential \  
software-properties-common \  
unzip \  
wget \  
vim \  
libpng-dev \  
libfreetype6-dev \  
libasound-dev \  
portaudio19-dev \  
libportaudio2 \  
libportaudiocpp0 \  
ffmpeg && \  
apt-get clean  
  
# Remove apt-cache  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install essential pip packages  
RUN pip install -U pip setuptools && \  
pip install \  
numpy \  
scipy \  
scikit-learn \  
pandas \  
matplotlib \  
jupyter \  
theano  
  
# Some of packages break without their dependencies  
# hence, seperating them out to ensure their dependencies  
# exist before them.  
RUN pip install pydub \  
pyaudio \  
nussl \  
librosa \  
peakutils \  
mir_eval \  
pysptk \  
sidekit  
  
# Install non-pip packages  
## Auditok  
RUN wget -q https://github.com/amsehili/auditok/archive/master.zip -O
/tmp/auditok.zip && \  
unzip /tmp/auditok.zip -d /tmp/ && \  
cd /tmp/auditok-master/ && \  
python setup.py install  
  
## pyAcoustics  
RUN wget -q https://github.com/timmahrt/pyAcoustics/archive/master.zip -O
/tmp/pyAcoustics.zip && \  
unzip /tmp/pyAcoustics.zip -d /tmp/ && \  
cd /tmp/pyAcoustics-master/ && \  
python setup.py install  
  
# Tini operates as a process subreaper for jupyter.  
# This prevents kernel crashes.  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
# Expose ports & volumes  
VOLUME /appdata  
EXPOSE 8888  
WORKDIR /appdata  
  
COPY jupyter_notebook_config.py /root/.jupyter/  
COPY start_jupyter.sh /  
RUN chmod +x /start_jupyter.sh  
  
CMD ["/start_jupyter.sh"]  
  

