FROM vvakame/review  
MAINTAINER kokuyouwind <kokuyouwind@gmail.com>  
  
# install Graph Tools(Graphviz, gnuplot)  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gnuplot graphviz python-aafigure && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# install Graph Tools(blockdiag, aafigure)  
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python && \  
pip install reportlab && \  
pip install blockdiag  

