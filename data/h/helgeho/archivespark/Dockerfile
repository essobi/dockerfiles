FROM continuumio/anaconda3  
MAINTAINER holzmann@L3S.de  
  
# Install Jupyter  
RUN conda install jupyter -y --quiet  
  
# Install Java  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y -t jessie-backports openjdk-8-jre  
  
# Copy files  
COPY jupyter_notebook_config.py /jupyter_notebook_config.py  
  
COPY setup.sh /setup.sh  
RUN chmod +x /setup.sh  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
COPY kernel.json /kernel.json  
  
# Setup and run  
VOLUME /config  
VOLUME /notebooks  
EXPOSE 8888  
CMD ["sh", "/setup.sh"]

