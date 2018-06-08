FROM tsutomu7/ubuntu-essential  
  
ENV PATH=/opt/conda/bin:$PATH \  
LANG=C.UTF-8 \  
DEBIAN_FRONTEND=noninteractive \  
MINICONDA=Miniconda2-latest-Linux-x86_64.sh  
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends
\  
libglib2.0-0 libxext6 libsm6 libxrender1 expat libltdl7 busybox wget fonts-
ipaexfont && \  
/bin/busybox --install && \  
apt-get clean && \  
echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget -q --no-check-certificate \  
https://repo.continuum.io/miniconda/$MINICONDA && \  
bash /$MINICONDA -b -p /opt/conda && \  
conda update -y conda && \  
conda install -y nomkl pandas matplotlib networkx jupyter ncurses lxml && \  
conda install -y -c https://conda.anaconda.org/pdrops pygraphviz && \  
pip install more-itertools bs4 bottlenose wikipedia && \  
ln -s /usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf \  
/opt/conda/lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf/ && \  
find /opt -name *.py[co] | xargs rm -r && \  
rm -rf /var/lib/apt/lists/* /$MINICONDA /root/.c* /opt/conda/pkgs/*  
ADD MonkeyBench.tgz /opt/conda/lib/python2.7/site-packages/  
COPY sample.tgz /tmp/  
COPY jupyter_notebook_config.py /root/.jupyter/  
EXPOSE 8888  
VOLUME ["/jupyter"]  
WORKDIR /jupyter  
CMD ["sh", "-c", "tar zxzf /tmp/sample.tgz && jupyter notebook --ip=*"]  

