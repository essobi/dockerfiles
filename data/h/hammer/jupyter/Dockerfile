From jupyter/scipy-notebook  
  
MAINTAINER "takemi.ohama" <takemi.ohama@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
wget curl ssh libreadline-dev vim \  
lsb-release \  
libxrender1 \  
mysql-client \  
language-pack-ja-base language-pack-ja fonts-mplus \  
graphviz  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
echo "export VISIBLE=now" >> /etc/profile && \  
echo "export TERM=xterm" >> /etc/profile && \  
echo "jovyan ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jovyan  
  
RUN update-locale LANGUAGE=ja_JP:ja LANG=ja_JP.UTF-8  
  
# Install Python 3 packages  
RUN conda install --quiet --yes \  
'conda-build' \  
'readline' \  
'python-dotenv' \  
'mysql-connector-python' \  
'pymysql' \  
'psycopg2' \  
'sqlalchemy-redshift' \  
'gensim' \  
'pivottablejs' \  
'jupyterlab' \  
'jupyterhub' \  
'xgboost' \  
'tensorflow' \  
'imbalanced-learn' \  
'flask' \  
&& conda clean -tipsy  
  
USER $NB_USER  
  
RUN /opt/conda/bin/pip install --upgrade pip graphviz  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  

