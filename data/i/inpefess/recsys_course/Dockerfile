FROM ubuntu:artful  
# install all needed packages, system and Python  
RUN apt-get update && apt-get install default-jre-headless \  
python3-pip git wget unzip htop -y && \  
pip3 install pyspark jupyter numpy pandas matplotlib seaborn \  
jupyterlab RISE scikit-learn scipy loglikelihood implicit \  
pyarrow annoy lightfm  
# surprise won't install without numpy preinstalled  
RUN pip3 install scikit-surprise  
RUN jupyter-nbextension install rise --py --sys-prefix && \  
jupyter-nbextension enable rise --py --sys-prefix  
# get the data  
WORKDIR /data  
RUN wget http://files.grouplens.org/datasets/movielens/ml-latest.zip && \  
unzip ml-latest.zip && rm ml-latest.zip && \  
wget http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-360K.tar.gz \  
&& tar -xvf lastfm-dataset-360K.tar.gz && rm lastfm-dataset-360K.tar.gz  
# get the code  
COPY . /code  
# prepare the environment  
WORKDIR /code  
ENV JAVA_HOME=/usr/lib/jvm/default-java  
ENV PYSPARK_PYTHON=python3  
ENV PYTHONPATH=/code:$PYTHONPATH  
ENV SHELL=/bin/bash  
EXPOSE 4040  
EXPOSE 8888  
CMD ["jupyter-notebook", "--no-browser", "--allow-root"]  

