FROM python:3.5.1  
RUN pip install -U setuptools pip  
RUN pip install sphinx==1.4.6 Pillow  
RUN mkdir -p /doc  
WORKDIR /doc  
VOLUME /doc  
  
CMD ["sphinx-build", "-M", "html", "/doc/", "/doc/_build", "-N"]  
  

