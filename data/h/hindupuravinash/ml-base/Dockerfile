FROM ubuntu  
  
MAINTAINER Aviansh Hindupur  
  
RUN apt-get update && apt-get -y install wget bzip2 python3.5  
  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh
-O ./miniconda.sh && \  
bash ./miniconda.sh -b -p /opt/conda  
  
ENV PATH /opt/conda/bin:$PATH  
  
  
RUN conda install -y \  
jupyter \  
matplotlib \  
nltk \  
seaborn \  
scikit-learn  
  
RUN useradd -ms /bin/bash avi  
USER avi  
WORKDIR /home/avi  
  
EXPOSE 8888  
CMD jupyter notebook --port=8888 --ip=0.0.0.0  
  
#CMD [ "/bin/bash" ]  

