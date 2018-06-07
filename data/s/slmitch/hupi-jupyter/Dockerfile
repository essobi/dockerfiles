FROM jupyter/all-spark-notebook:c7d997f2db86  
  
USER root  
  
RUN mkdir -p /opt  
RUN curl -L
http://apache.crihan.fr/dist/hadoop/common/hadoop-2.7.6/hadoop-2.7.6.tar.gz |
tar -xz -C /opt/ && mv /opt/hadoop-2.7* /opt/hadoop  
  
USER $NB_UID  
  
# R packages  
RUN conda install --quiet --yes \  
'r-base=3.4.1' \  
'r-irkernel=0.7*' \  
'r-plyr=1.8*' \  
'r-devtools=1.13*' \  
'r-tidyverse=1.1*' \  
'r-shiny=1.0*' \  
'r-rmarkdown=1.8*' \  
'r-forecast=8.2*' \  
'r-rsqlite=2.0*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-crayon=1.3*' \  
'r-randomforest=4.6*' \  
'r-htmltools=0.3*' \  
'r-sparklyr=0.7*' \  
'r-htmlwidgets=1.0*' \  
'r-hexbin=1.27*' \  
'r-doParallel' \  
'r-rjava' \  
'nb_conda' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
RUN conda install --quiet --yes -c cyclus java-jdk && conda clean -tipsy &&
fix-permissions $CONDA_DIR && fix-permissions /home/$NB_USER  
RUN conda install --quiet --yes -c terradue r-rhdfs r-rgdal && conda clean
-tipsy && fix-permissions $CONDA_DIR && fix-permissions /home/$NB_USER  
RUN conda install --quiet --yes -c bioconda 'r-mixomics' && conda clean -tipsy
&& fix-permissions $CONDA_DIR && fix-permissions /home/$NB_USER  
RUN conda create -n python2 python=2.7 ipykernel && conda clean -tipsy && fix-
permissions $CONDA_DIR && fix-permissions /home/$NB_USER  
RUN conda install --quiet --yes -c christophaburke r-rpostgresql && conda
clean -tipsy && fix-permissions $CONDA_DIR && fix-permissions /home/$NB_USER  
  
RUN ipython profile create pyspark  
  

