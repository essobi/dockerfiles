FROM mediadesignpractices/debian:latest  
LABEL organization "Media Design Practices"  
LABEL maintainer "mediadesignpractices"  
LABEL contributor "unsalted"  
USER root  
RUN groupadd \--gid 8000 python \  
&& usermod -a -G python mdp  
  
# change python version in mdp:latest  
ENV PYTHON_PIP_VERSION 9.0.1  
ENV PYTHON_VERSION $PYTHON2_VERSION  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN pip \--no-cache-dir install \  
virtualenv \  
requests \  
matplotlib \  
numpy \  
flask \  
scipy \  
pandas \  
Pillow \  
beautifulsoup4  
  
USER $NB_USER  
WORKDIR $WORK_DIR  
  
CMD ["python2"]  

