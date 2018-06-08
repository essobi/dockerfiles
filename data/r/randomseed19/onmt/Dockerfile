FROM randomseed19/babel_fairseq  
  
RUN git clone https://github.com/OpenNMT/OpenNMT-py.git  
RUN cd /OpenNMT-py && /opt/conda/bin/pip install -r requirements.txt &&
/opt/conda/bin/python setup.py install

