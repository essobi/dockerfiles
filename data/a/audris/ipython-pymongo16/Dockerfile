FROM jupyter/scipy-notebook  
  
MAINTAINER Jupyter Project <jupyter@googlegroups.com>  
  
USER root  
  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" > /etc/apt/sources.list.d/mongodb-org-3.0.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9ECBEC467F0CEB10  
  
RUN conda install --quiet --yes \  
'pyqt=4.11*' \  
'pymongo=3.3*' \  
'beautifulsoup4=4.4*' \  
'nltk=3.2*' \  
&& conda clean -tipsy  
  
RUN conda install --quiet --yes \  
\--channel https://conda.anaconda.org/mutirri \  
'gensim=0.12*' \  
&& conda clean -tipsy  
  
# R pre-requisites  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
fonts-dejavu \  
gfortran \  
g++ \  
libopenblas-base && apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y \  
mariadb-client \  
mariadb-common \  
mongodb-org-shell \  
mysql-common \  
openssh-server \  
sssd \  
sssd-tools \  
sqlite3 \  
vim \  
vim-runtime \  
tmux \  
zsh \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# R packages including IRKernel which gets installed globally.  
RUN conda config --add channels r && \  
conda install --quiet --yes \  
'rpy2=2.8*' \  
'r-base=3.3*' \  
'r-irkernel=0.6*' \  
'r-plyr=1.8*' \  
'r-devtools=1.11*' \  
'r-dplyr=0.4*' \  
'r-ggplot2=2.1*' \  
'r-tidyr=0.5*' \  
'r-shiny=0.13*' \  
'r-rmarkdown=0.9*' \  
'r-forecast=7.1*' \  
'r-stringr=1.0*' \  
'r-rsqlite=1.0*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-randomforest=4.6*' && conda clean -tipsy  
  
ENV LC_ALL C.UTF-8  
#install ldap authentication to use utk's ldap  
RUN /opt/conda/bin/python -m nltk.downloader -d /usr/share/nltk_data stopwords
wordnet gutenberg words  
COPY eecsCA_v3.crt /etc/ssl/  
COPY sssd.conf /etc/sssd/  
COPY common* /etc/pam.d/  
RUN chmod 0600 /etc/sssd/sssd.conf /etc/pam.d/common*  
RUN mkdir -p /var/run/sshd  
RUN chmod 0755 /var/run/sshd  
  
RUN mv /opt/conda/lib/R/lib/libRblas.so /opt/conda/lib/R/lib/libRblas.so.old  
RUN ln -s /usr/lib/libblas.so.3 /opt/conda/lib/R/lib/libRblas.so  
  
COPY init.sh /bin/  
COPY startsvc.sh /bin/  
COPY notebook.sh /bin/  

