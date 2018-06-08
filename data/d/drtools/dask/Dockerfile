FROM drtools/scientific  
  
USER root  
RUN curl -L https://github.com/rilian-la-te/musl-locales/archive/master.tar.gz
| tar xz && \  
cd musl-locales-master/ && \  
apk add --no-cache --virtual .build-dependencies cmake make gcc musl-dev
gettext-dev && \  
cmake . && make && make install  
USER drtools  
  
RUN conda install -y \  
lz4 \  
psutil \  
tornado \  
pandas \  
dask \  
distributed \  
fastparquet \  
s3fs \  
python-blosc \  
gcsfs && \  
conda clean -tipsy && \  
rm -rf /opt/conda/pkgs/*  
  

