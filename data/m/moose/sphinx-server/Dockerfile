FROM python:3.6-alpine  
RUN pip install sphinx sphinx-autobuild recommonmark sphinx_rtd_theme  
COPY bootstrap.sh /bootstrap.sh  
CMD mkdir /docs  
WORKDIR /docs  
EXPOSE 8000  
CMD /bootstrap.sh  

