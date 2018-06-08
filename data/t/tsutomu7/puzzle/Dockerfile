FROM ubuntu-debootstrap:14.04  
RUN apt-get update --fix-missing && apt-get install -y \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
ca-certificates busybox wget && \  
/bin/busybox --install && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ENV PATH=/opt/conda/bin:$PATH \  
LANG=C.UTF-8 \  
MINICONDA=Miniconda3-latest-Linux-x86_64.sh  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/$MINICONDA && \  
bash /$MINICONDA -b -p /opt/conda && \  
conda install -y conda && \  
conda update -y conda && \  
conda install -y jupyter && \  
pip install pulp unionfind && \  
rm -rf $MINICONDA /opt/conda/pkgs/*  
EXPOSE 8888  
VOLUME ["/jupyter"]  
WORKDIR /jupyter  
COPY puzzle.tar.gz /root/  
CMD ["sh", "-c", "tar xzf /root/puzzle.tar.gz -C /jupyter && jupyter notebook
--ip=*"]  

