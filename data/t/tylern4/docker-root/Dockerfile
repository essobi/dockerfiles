FROM tylern4/rootv6:centos7  
LABEL maintainer "tylern@jlab.org"  
  
RUN pip install --upgrade pip setuptools \  
&& pip --no-cache-dir install -U \  
rootpy \  
numpy \  
pandas \  
matplotlib \  
scipy \  
scikit-learn \  
ipyparallel \  
sqlalchemy \  
pymongo \  
mpi4py \  
numba \  
termcolor \  
colorama \  
tqdm \  
cython \  
iminuit \  
rootpy \  
numpy \  
pandas \  
dask \  
bokeh \  
networkx \  
plotly \  
brewer2mpl \  
seaborn \  
root2matplot \  
ggplot \  
odo  
  
RUN ROOTSYS=$ROOTSYS pip install root-numpy  
  
COPY zshrc /root/.zshrc  
copy oh-my-zsh /root/.oh-my-zsh  
  
WORKDIR /root/code  
  
ENTRYPOINT ["/bin/zsh"]  

