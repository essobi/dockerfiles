FROM jfloff/alpine-python:2.7  
LABEL maintainer="jfloff@inesc-id.pt"  
  
RUN set -ex ;\  
echo "@community http://dl-
cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/community" >>
/etc/apk/repositories ;\  
apk add --update --no-cache \  
# for matplotlib  
freetype-dev \  
tini@community \  
#for seaborn  
gfortran \  
openblas-dev@community \  
# for lxml  
libxslt-dev \  
py-lxml \  
# for jupyter  
sqlite \  
sqlite-dev \  
socat \  
;\  
rm /var/cache/apk/*  
  
RUN set -ex ;\  
pip install --upgrade --no-cache-dir numpy \  
scipy \  
pandas \  
matplotlib \  
seaborn \  
# needed for jupyter  
pysqlite \  
jupyter \  
lxml \  
;\  
pip install --upgrade --no-cache-dir scikit-learn \  
;\  
# make sure nothing is on pip cache folder  
rm -rf ~/.cache/pip/  
# setup jupyter  
ENV JUPYTER_PATH=/home/jupyter \  
JUPYTER_PORT=8888  
EXPOSE $JUPYTER_PORT  
RUN set -ex ;\  
jupyter notebook --generate-config --allow-root ;\  
sed -i -e "s/#c.NotebookApp.ip .*/c.NotebookApp.ip = '0.0.0.0'/g"
/root/.jupyter/jupyter_notebook_config.py ;\  
sed -i -e "s/#c.NotebookApp.port .*/c.NotebookApp.port = $JUPYTER_PORT/g"
/root/.jupyter/jupyter_notebook_config.py ;\  
sed -i -e "s/#c.NotebookApp.allow_root .*/c.NotebookApp.allow_root = True/g"
/root/.jupyter/jupyter_notebook_config.py ;\  
sed -i -e "s/#c.NotebookApp.token .*/c.NotebookApp.token = u''/g"
/root/.jupyter/jupyter_notebook_config.py  
  
# for jupyter  
ENTRYPOINT ["/sbin/tini", "--"]

