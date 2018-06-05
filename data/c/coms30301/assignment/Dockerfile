FROM continuumio/anaconda:4.2.0  
MAINTAINER Kacper Sokol <ks1591@bristol.ac.uk>  
  
ENV NOTEBOOKS /opt/notebooks  
  
RUN /opt/conda/bin/conda install jupyter -y --quiet \  
&& mkdir $NOTEBOOKS  
  
RUN git clone https://github.com/COMS30301/assignment_1.git
$NOTEBOOKS/assignment_1 \  
&& git clone https://github.com/COMS30301/lab_3.git $NOTEBOOKS/lab_3  
  
RUN cd $NOTEBOOKS/lab_3 \  
&& git checkout tags/v0.1.0  
  
RUN git clone https://github.com/COMS30301/spam.git $HOME/spam  
  
WORKDIR $HOME  

