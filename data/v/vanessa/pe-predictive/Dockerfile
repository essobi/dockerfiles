FROM ubuntu:15.10  
MAINTAINER Vanessa Sochat <vsochat@stanford.edu>  
  
RUN apt-get update && apt-get install -y \  
cython3 \  
gcc \  
ipython3-notebook \  
mc \  
nano \  
git \  
python3 \  
python3-numpy \  
python3-pip \  
python3-setuptools \  
python3-scipy \  
vim  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV CODE_HOME /code  
RUN easy_install3 --upgrade gensim  
RUN apt-get install -y python3-pandas  
RUN apt-get install -y python3-numpy  
RUN apt-get install -y python3-scipy  
RUN pip3 install scikit-learn  
RUN pip3 install wordfish  
RUN git clone https://github.com/chapmanbe/pyConTextNLP  
WORKDIR pyConTextNLP  
RUN python3 setup.py install  
RUN python3 -c "import nltk; nltk.download('all')"  
RUN pip3 install radnlp  
  
# Add aliases to .bashrc to not need to specify python3  
RUN echo "alias python='python3'" >> ~/.bashrc  
RUN echo "alias ipython='ipython3'" >> ~/.bashrc  
RUN echo "alias pip='pip3'" >> ~/.bashrc  
  
RUN mkdir /code  
WORKDIR /code  
  
EXPOSE 9000  
CMD ["/bin/bash"]  

