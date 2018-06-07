FROM quay.io/fenicsproject/dev-py3:latest  
EXPOSE 8888  
  
ENV PYTHON=python3  
  
USER root  
# base packages  
RUN apt-get -y update && apt-get -y install libzmq3-dev libfreetype6-dev
libpng-dev $PYTHON-scipy  
RUN $PYTHON -m pip install --upgrade setuptools pip  
  
# Python dependencies for the notebook  
ADD requirements.txt /tmp/requirements.txt  
RUN $PYTHON -m pip install -r /tmp/requirements.txt  
  
USER fenics  
# something about the fenics entrypoint means this only works as a single
string  
# instead of a normal command list  
CMD [ "jupyter notebook --no-browser --ip=*" ]  

