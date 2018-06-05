FROM strawberrypie/pytorch-cuda8:v0.3  
RUN git clone https://github.com/OpenNMT/OpenNMT-py.git && cd OpenNMT-py &&
pip install -r requirements.txt && python setup.py install  
RUN curl -s -L
https://gist.githubusercontent.com/Khakhulin/cba862fe6cd9f9f2a0cc2ad87d1b6325/raw/aec288230ac12a662bec55524fd52edefeb04387/run.sh
-o ~/run.sh && chmod +x ~/run.sh  
RUN curl -s -L
https://gist.github.com/strawberrypie/ba1f630f17d59f71862417565ceaa6f8/raw -o
~/split_parallel_corpus.py && chmod +x ~/split_parallel_corpus.py  
RUN pip install gensim nltk  
RUN python -m nltk.downloader punkt

