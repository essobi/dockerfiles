FROM python:3.5  
RUN git clone https://github.com/lovelylain/pyctp.git && \  
cd pyctp && \  
python setup.py install && \  
cd .. && \  
rm -rf pyctp  
  
COPY $PWD /easyctp  
  
RUN pip install -r /easyctp/requirements.txt && \  
cd easyctp && \  
python setup.py install  
  
WORKDIR /easyctp  
  
ENTRYPOINT ["python", "scripts/subscribe_ctp_to_influxdb.py"]  
  

