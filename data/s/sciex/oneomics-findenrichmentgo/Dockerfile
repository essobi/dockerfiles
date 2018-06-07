FROM sciex/docker-base-python-image:2017.02.22  
RUN \  
apt-get update && \  
apt-get install -y python-numpy python-scipy python-matplotlib ipython
ipython-notebook python-pandas python-sympy python-nose && \  
easy_install fisher && \  
pip install flask_restful waitress  
  
RUN \  
curl http://geneontology.org/ontology/go-basic.obo -o /home/app/go-basic.obo
&& \  
curl http://geneontology.org/ontology/subsets/goslim_generic.obo -o
/home/app/goslim_generic.obo  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV SERVICE_NAME enrichment  
  
ADD . /docker/app  
WORKDIR /docker/app  
  
EXPOSE 80  
CMD ["python", "api.py"]  

