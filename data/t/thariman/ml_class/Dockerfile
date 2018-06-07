FROM python:2.7  
  
MAINTAINER Tony Hariman <thariman@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
wget \  
unzip  
  
RUN pip install --no-cache-dir "nltk == 3.2.1" && \  
pip install --no-cache-dir "numpy == 1.11.1" && \  
pip install --no-cache-dir "hcluster == 0.2.0" && \  
pip install --no-cache-dir "scipy == 0.18.0" && \  
pip install --no-cache-dir "sklearn" && \  
pip install --no-cache-dir "pylab" && \  
pip install --no-cache-dir "python-hashes"  
RUN wget --quiet
"http://bonsai.hgc.jp/~mdehoon/software/cluster/Pycluster-1.52.tar.gz" && \  
tar -xzf Pycluster-1.52.tar.gz && \  
cd Pycluster-1.52 && \  
python setup.py install && \  
cd .. && \  
rm -rf /root/Pycluster-1.52 /root/Pycluster-1.52.tar.gz  
  
RUN wget --quiet "https://raw.githubusercontent.com/nltk/nltk_data/gh-
pages/packages/tokenizers/punkt.zip" && \  
mkdir -p /root/nltk_data/tokenizers && \  
unzip punkt.zip -d /root/nltk_data/tokenizers/ && \  
rm -rf punkt.zip  
  
WORKDIR /root  
  
# Code for Hilary Mason: An Introduction to Machine Learning with Web Data  
# http://shop.oreilly.com/product/0636920017493.do  
# Code for Hilary Mason: Advanced Machine Learning  
# http://shop.oreilly.com/product/0636920025610.do  
RUN git clone https://github.com/hmason/ml_class.git  
  
  
# cleanup  
RUN apt-get remove -y libncurses5-dev && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
  
CMD [ "/bin/bash" ]  

