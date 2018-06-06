FROM continuumio/anaconda3  
  
RUN apt-get update  
  
# Install software dependencies  
RUN apt-get -y install graphviz  
RUN pip install radnlp==0.2.0.8  
RUN pip install seaborn==0.7.1  
RUN pip install pydotplus  
RUN pip install nltk  
  
# Install jupyter notebook  
RUN /opt/conda/bin/conda install jupyter -y --quiet  
RUN /opt/conda/bin/python -m nltk.downloader -d /usr/local/share/nltk_data all  
  
RUN mkdir /code  
RUN mkdir /data  
  
# Add the code  
ADD . /code  
WORKDIR /code/pefinder  
  
# Clean up  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN chmod u+x /code/pefinder/cli.py  
  
ENTRYPOINT ["python","/code/pefinder/cli.py"]  

