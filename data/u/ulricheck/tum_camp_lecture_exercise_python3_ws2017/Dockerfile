FROM continuumio/anaconda3:latest  
MAINTAINER Ulrich Eck (firstname.lastname@tum.de)  
  
  
  
RUN /opt/conda/bin/conda install jupyter -y --quiet  
RUN mkdir /opt/notebooks  
  
# install custom packages  
RUN /opt/conda/bin/conda install opencv -y --quiet  
RUN /opt/conda/bin/pip install pydicom --quiet  
  
VOLUME /opt/notebooks  
EXPOSE 8888  
CMD /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*'
\--port=8888 --no-browser --allow-root  

