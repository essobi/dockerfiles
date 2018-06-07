FROM insectatorious/machine-learning:python-scikit-nltk  
  
MAINTAINER Sumanas Sarma <insectatorious+docker@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y libblas-dev checkinstall && \  
apt-get install -y libblas-doc checkinstall && \  
apt-get install -y liblapacke-dev checkinstall && \  
apt-get install -y liblapack-doc checkinstall  
  
RUN /usr/bin/yes | pip install -U Cython numpy pandas scikit-learn nltk tsne  
  
  

