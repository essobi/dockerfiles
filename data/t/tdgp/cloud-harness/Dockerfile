FROM sparkgeo/geospatial-base:latest  
  
ADD . /root/cloud-harness/  
  
WORKDIR /root/cloud-harness  
RUN pip install setuptools wheel  
RUN python setup.py bdist_wheel --universal  
RUN pip install dist/*.whl  
  
RUN mkdir /root/runner/  
  
ADD ./docker_runner/application_runner.py /root/runner/application_runner.py  
  
ENV PYTHONPATH="."  
ENV REMOTE_WORK_PATH="/mnt/work"  
CMD ["python", "/root/runner/application_runner.py"]  

