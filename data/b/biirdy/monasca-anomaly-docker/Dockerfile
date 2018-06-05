FROM monasca/demo  
MAINTAINER Jamie Bird <j.bird1@lancaster.ac.uk>  
  
#new start script  
COPY ./anomaly-start.sh /setup/  
RUN chmod 755 /setup/anomaly-start.sh  
  
#monasca-anomaly  
WORKDIR /  
RUN git clone https://github.com/biirdy/monasca-anomaly.git  
  
WORKDIR /monasca-anomaly  
RUN pip install numpy  
RUN apt-get install -y libatlas-base-dev gfortran  
RUN pip install https://s3-us-
west-2.amazonaws.com/artifacts.numenta.org/numenta/nupic.core/releases/nupic.bindings/nupic.bindings-0.1.5-cp27-none-
linux_x86_64.whl  
RUN pip install -r requirements.txt  
RUN python setup.py install  
  
RUN apt-get clean  
  
#remove tail from old start script  
RUN sed -i '/tail -f/d' /setup/demo-start.sh  
  
#apache, keystone, keystone, monasca api  
EXPOSE 80 5000 35357 8080  
CMD ["/setup/anomaly-start.sh"]  

