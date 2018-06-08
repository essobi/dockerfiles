FROM jupyter/datascience-notebook  
  
# Based on the Jupyter DataScience Notebook  
#  
# https://github.com/jupyter/docker-stacks/blob/master/minimal-
notebook/Dockerfile  
# https://github.com/jupyter/docker-stacks/blob/master/datascience-
notebook/Dockerfile  
#  
MAINTAINER Chris Baker <ignatz@gmail.com>  
  
user root  
  
ENV PY2_DIR $CONDA_DIR/envs/python2  
  
RUN apt-get update && apt-get install -y apt-utils  
  
# Add LilyPond Stable  
# http://www.lilypond.org/  
RUN apt-get install -y lilypond  
  
# Upgrade pip  
RUN pip install --upgrade pip  
RUN $PY2_DIR/bin/pip install --upgrade pip  
  
# Add PyAudio  
RUN apt-get install -y portaudio19-dev  
RUN pip install pyaudio  
RUN $PY2_DIR/bin/pip install pyaudio  
  
# install Music21  
RUN pip install music21  
RUN $PY2_DIR/bin/pip install music21  
  
# Install Python Imaging Library  
RUN pip install image  
#RUN $PY2_DIR/bin/pip install image  
# Install Pygame  
RUN apt-get install -y mercurial  
RUN apt-get install -y libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-
ttf2.0-dev libsmpeg-dev libportmidi-dev  
RUN apt-get install -y libswscale-dev libavformat-dev wget curl mc  
RUN hg clone https://bitbucket.org/pygame/pygame  
RUN cd pygame && python2.7 setup.py build && python2.7 setup.py install && cd
.. && rm -rf pygame  
  
# Pygame Python 3 install - Does this next bit work?!  
RUN hg clone https://bitbucket.org/pygame/pygame  
RUN cd pygame && python setup.py build && python setup.py install && cd .. &&
rm -rf pygame  
  
# GDAL  
RUN pip install pyproj  
RUN $PY2_DIR/bin/pip install pyproj  
  
RUN conda install --yes basemap pillow && conda clean -yt  
  
# Upgrade matplotlib to 1.5 to remove errors introduced in 1.4.3  
# NO LONGER NEEDED  
# RUN pip install --upgrade matplotlib  
# RUN $PY2_DIR/bin/pip install --upgrade matplotlib  
## Upgrade pip AGAIN?!!! Why does it need to do it twice??!  
#RUN pip install --upgrade pip  
#RUN $PY2_DIR/bin/pip install --upgrade pip  
#  
#RUN pip install httpretty  
#RUN pip install boto  
#RUN pip install bz2file  
#RUN pip install requests  
#RUN pip install smart-open --no-dependencies  
#  
## Gensim  
## https://radimrehurek.com/gensim/intro.html  
#RUN pip install gensim --no-dependencies  
#  
## NLTK  
#RUN pip install nltk  
# RUN ME  
# RUN python -m nltk.downloader all  
# RUN $PY2_DIR/bin/pip install nltk  
# To install or upgrade MuseScore:  
RUN apt-get install -y musescore

