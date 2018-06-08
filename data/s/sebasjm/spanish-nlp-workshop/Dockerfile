FROM continuumio/anaconda3  
  
MAINTAINER Sebastian Marchano <sebasjm@gmail.com>  
  
RUN mkdir /opt/notebooks  
WORKDIR /opt/notebooks  
  
RUN conda config --add channels conda-forge  
RUN conda create -y -n nlp python=3 gensim spacy matplotlib scikit-learn
pandas ipykernel  
RUN apt-get update --fix-missing && apt-get install -y libgomp1 unzip
python3-pip  
RUN /bin/bash -c "source activate nlp; python3 -m pip install bs4"  
RUN /bin/bash -c "source activate nlp; python3 -m spacy download es"  
RUN /bin/bash -c "source activate nlp; /opt/conda/bin/conda install jupyter -y
--quiet"  
RUN /bin/bash -c "source activate nlp; python3 -m ipykernel install --user"  
  
COPY spanish-nlp.ipynb /opt/notebooks  
COPY start.sh /start.sh  
  
RUN mkdir /root/.jupyter  
COPY jupyter_notebook_config.py /root/.jupyter  
  
EXPOSE 8888  
CMD ["/bin/bash","/start.sh"]  

