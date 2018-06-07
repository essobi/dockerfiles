FROM continuumio/miniconda3  
MAINTAINER tiagoantao@gmail.com  
  
RUN /opt/conda/bin/conda install jupyter matplotlib networkx -y  
RUN mkdir /test  
  
VOLUME ['/test']  
EXPOSE 8888  
CMD /opt/conda/bin/jupyter notebook --notebook-dir=/test \--ip='*'
\--port=8888 --no-browser  

