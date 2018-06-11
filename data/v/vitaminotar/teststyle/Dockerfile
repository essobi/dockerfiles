FROM strawberrypie/pytorch-cuda8:v0.3  
RUN git clone https://github.com/OpenNMT/OpenNMT-py.git && cd OpenNMT-py &&
pip install -r requirements.txt && python setup.py install  
RUN pip install gensim nltk  
RUN python -m nltk.downloader punkt

