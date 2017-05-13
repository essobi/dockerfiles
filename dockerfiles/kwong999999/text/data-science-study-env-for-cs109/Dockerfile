FROM python:2.7-slim
MAINTAINER Jack Kwong

RUN apt-get update && \
    apt-get install -y --fix-missing curl git vim build-essential python-dev pkg-config libfreetype6-dev libpng-dev libblas-dev liblapack-dev gfortran libxml2-dev libxslt1-dev libjpeg62-turbo-dev r-base && \
    apt-get clean && \
    pip install notebook ipykernel pandas numpy scipy seaborn pyquery beautifulsoup4 numexpr requests scikit-learn statsmodels Pillow simplejson gensim rpy2 findspark secret && \
    apt-get autoremove -y --purge build-essential python-dev pkg-config libfreetype6-dev libpng-dev libblas-dev liblapack-dev gfortran libxml2-dev libxslt1-dev libjpeg62-turbo-dev 

RUN mkdir -p /root/notebooks/course
WORKDIR /root/notebooks/course

RUN git clone https://github.com/cs109/2015lab1 && \
    git clone https://github.com/cs109/2015lab2 && \
    git clone https://github.com/cs109/2015lab3 && \
    git clone https://github.com/cs109/2015lab4 && \
    git clone https://github.com/cs109/2015lab5 && \
    git clone https://github.com/cs109/2015lab6 && \
    git clone https://github.com/cs109/2015lab7 && \
    git clone https://github.com/cs109/2015lab8 && \
    git clone https://github.com/cs109/2015lab9 && \
    git clone https://github.com/cs109/2015lab10 && \
    git clone https://github.com/cs109/2015lab11 && \
    git clone https://github.com/cs109/cs109_data && \
    git clone https://github.com/cs109/2015.git

CMD /bin/bash -c "jupyter notebook --NotebookApp.ip='*' --MultiKernelManager.default_kernel_name='py2' -y --no-browser --notebook-dir='/root/notebooks' --port=8888"

EXPOSE 8888
