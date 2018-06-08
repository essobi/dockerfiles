FROM continuumio/anaconda3  
MAINTAINER sshy  
EXPOSE 8080  
RUN conda update conda && conda install numpy scipy scikit-learn matplotlib
pandas  
  
RUN pip install Theano && pip install keras  
RUN conda install -c conda-forge tensorflow  
  
RUN /opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks  
  
ENTRYPOINT /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks
--ip='*' \--port=8080 --no-browser  

