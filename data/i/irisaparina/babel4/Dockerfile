FROM strawberrypie/pytorch-cuda8:v0.3  
  
RUN git clone https://github.com/OpenNMT/OpenNMT-py.git && cd OpenNMT-py &&
pip install -r requirements.txt && python setup.py install  
RUN curl -s -L
https://raw.githubusercontent.com/saparina/babel4/master/run.sh?token=AVTxeLqFGT7RRLD88txZFp9JUjnV7Imgks5afJmfwA%3D%3D
-o ~/run.sh && chmod +x ~/run.sh  
RUN curl -s -L
https://gist.github.com/strawberrypie/ba1f630f17d59f71862417565ceaa6f8/raw -o
~/split_parallel_corpus.py && chmod +x ~/split_parallel_corpus.py  
RUN curl -s -L
https://gist.githubusercontent.com/saparina/a702c8e61d8e8ee7221d1ce724861b87/raw/66b37813abb7fe61f70ba3134527f71c135c9745/shuffling.py
-o ~/shuffling.py && chmod +x ~/shuffling.py  

