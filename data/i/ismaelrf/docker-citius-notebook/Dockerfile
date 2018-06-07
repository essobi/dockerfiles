FROM ipython/scipystack  
  
# Installing R  
RUN apt-get install -y \  
r-base \  
r-base-dev  
  
# Installing rpy2  
RUN pip install rpy2  
RUN pip install singledispatch  
RUN pip3 install rpy2  
  
# Installing python libraries  
RUN pip install BeautifulSoup4  
RUN pip3 install BeautifulSoup4  
RUN pip install nltk  
RUN pip3 install nltk  
  
# Creating service  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
# You can mount your own SSL certs as necessary here  
ENV PEM_FILE /key.pem  
  
ADD notebook.sh /  
RUN chmod u+x /notebook.sh  
  
ADD config.py /  
  
CMD ["/notebook.sh"]  

