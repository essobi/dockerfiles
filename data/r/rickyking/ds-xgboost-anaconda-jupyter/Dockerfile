FROM rickyking/ds-xgboost  
MAINTAINER Yi Jin <y.jin@me.com>  
  
  
RUN apt-get install -y wget bzip2 ca-certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
mercurial subversion  
WORKDIR /  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh
&& \  
/bin/bash /Anaconda2-4.0.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm /Anaconda2-4.0.0-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
RUN conda install -y -c https://conda.anaconda.org/anaconda setuptools  
RUN cd /opt/xgboost/python-package/ && python setup.py install  
ENV LANG C.UTF-8  
# Add a notebook profile.  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
# Install Tini  
ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENTRYPOINT ["tini", "--"]  
CMD ["jupyter", "notebook"]

