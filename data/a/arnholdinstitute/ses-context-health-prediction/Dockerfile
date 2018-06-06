FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
  
RUN apt-get update && apt-get install -y \--no-install-recommends build-
essential curl wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Install conda, python3, and some common dependencies  
RUN curl -o ~/miniconda.sh -O
https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh
\--insecure && \  
chmod +x ~/miniconda.sh && \  
~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && \  
/opt/conda/bin/conda install -y numpy scipy pandas matplotlib psycopg2 && \  
/opt/conda/bin/conda install -y pyqt=4.11 && \  
/opt/conda/bin/conda clean -ya  
  
RUN apt-get update && \  
apt-get install -y libxtst6 libsm6 libxrender1 libfontconfig1  
  
# Add conda to PATH  
ENV PATH /opt/conda/bin:$PATH  
  
# Install pytorch  
RUN conda install -y pytorch torchvision cuda80 -c soumith  
  
RUN mkdir /workspace  
  
RUN wget --no-check-certificate
https://gist.githubusercontent.com/ml9951/b543ffe77add831582744e5d96556148/raw/7fcd7b60630f7b79303ed4fd8916195ae60b242d/install.sh  
  
RUN head -n $(wc -l install.sh) | bash  
  
ENV PATH /root/bin:/root/.local/bin:$PATH  
  
RUN apt-get install -y git vim && \  
git clone https://github.com/patrick-dd/vimrc.git && \  
mv vimrc/.vimrc ~ && \  
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim  
  
COPY . /workspace  

