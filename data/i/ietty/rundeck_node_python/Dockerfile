From ietty/base-python  
  
MAINTAINER takemi.ohama<takemi.ohama@gmail.com>  
  
# Install Python 3 packages  
RUN conda install --quiet --yes \  
'conda-build' \  
'readline' \  
'ipywidgets' \  
'pandas' \  
'numexpr' \  
'matplotlib' \  
'scipy' \  
'seaborn' \  
'scikit-learn' \  
'scikit-image' \  
'sympy' \  
'cython' \  
'patsy' \  
'statsmodels' \  
'cloudpickle' \  
'dill' \  
'numba' \  
'bokeh' \  
'h5py' \  
'mysql-connector-python' \  
'pymysql' \  
'sqlalchemy' \  
'gensim' \  
'pivottablejs' \  
'jupyterlab' \  
&& conda clean -tipsy  
  
CMD ["/usr/sbin/sshd", "-D"]  

