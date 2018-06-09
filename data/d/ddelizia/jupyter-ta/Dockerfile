FROM jupyter/datascience-notebook  
  
LABEL maintainer="Danilo Delizia<ddelizia@gmail.com>"  
  
USER root  
  
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz &&
\  
tar xvfz ta-lib-0.4.0-src.tar.gz && \  
cd ta-lib && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
rm /home/jovyan/ta-lib-0.4.0-src.tar.gz && \  
rm -Rf /home/jovyan/ta-lib  
  
RUN apt-get update && apt-get -y install libatlas-base-dev python-dev gfortran
pkg-config libfreetype6-dev  
  
USER $NB_USER  
  
RUN pip install ta-lib  
RUN pip install zipline  
RUN pip install enigma-catalyst  
RUN pip install BeautifulSoup4  
RUN pip install tweepy  
RUN pip install praw  
RUN pip install textblob  
RUN pip install quandl  
RUN pip install plotly  
RUN pip install cufflinks  
RUN pip install git+https://github.com/oanda/oandapy.git  
RUN pip install ccxt  
  
# Install Tensorflow  
RUN conda install --quiet --yes \  
'tensorflow=1.3*' \  
'keras=2.0*' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  

