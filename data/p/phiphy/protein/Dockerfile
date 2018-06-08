FROM b.gcr.io/tensorflow/tensorflow-full  
  
RUN apt-get update  
RUN pip install --upgrade pip  
RUN pip install -U pip setuptools  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN TERM=linux apt-get install -y vim  
RUN sudo apt-get install -y python-numpy python-scipy python-matplotlib
python-pandas  
RUN pip install cython  
RUN pip install nose  
RUN pip install mdtraj  
RUN pip install --user MDAnalysis MDAnalysisTests  
RUN pip install -U scikit-learn  
RUN apt-get install -y git  
  
VOLUME /output  
  
WORKDIR /  
  
CMD bash  
  

