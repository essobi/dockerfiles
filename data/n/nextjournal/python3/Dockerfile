FROM continuumio/anaconda3:4.2.0  
  
RUN apt-get \--yes install libgomp1 && apt-get clean  
  
RUN conda config \--add channels omnia  
RUN conda install --yes -c omnia/label/pre pyemma  
RUN conda install --yes plotly matplotlib pyqt=4.11 seaborn  
RUN pip install --upgrade pip  
RUN pip install datapackage  
  
# to reduce startup time, build font cache for matplotlib  
RUN python -c "import matplotlib.pyplot, numpy as np, pickle, pyemma"  
  
COPY ./stream-stdin.py /scripts/stream-stdin.py  
COPY ./pyemma_logging.yml /root/.pyemma/logging.yml  

