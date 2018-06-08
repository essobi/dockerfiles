FROM python:3.6  
MAINTAINER pomupekun <pomupekun@gmail.com>  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive && apt-get install -yq \  
build-essential \  
git \  
texlive-fonts-recommended \  
texlive-latex-base && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
# RUN pip install jupyter --upgrade pip  
RUN pip install --upgrade pip && \  
pip3 --no-cache-dir install ipykernel && \  
pip3 --no-cache-dir install jupyter && \  
python3 -m ipykernel.kernelspec && \  
rm -rf /root/.cache  
EXPOSE 8888  
WORKDIR /notebook  
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--notebook-dir=/notebook", "--
config=/conf/jupyter_notebook_config.py"]  
  

