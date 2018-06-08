# Installs Jupyter Notebook and IPython kernel from the current branch  
# Another Docker container should inherit with `FROM jupyter/notebook`  
# to run actual services.  
FROM jupyter/scipy-notebook  
  
MAINTAINER Thorin Tabor <tmtabor@cloud.ucsd.edu>  
  
EXPOSE 8888  
# Upgrade ipywidgets  
RUN conda update ipywidgets widgetsnbextension -y  
  
USER root  
  
# Install ipywidgets' nbextension  
RUN jupyter nbextension install --py widgetsnbextension  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install the magic wrapper.  
RUN wget https://raw.githubusercontent.com/jpetazzo/dind/master/wrapdocker
--output-document=/usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Install the missing Qt4 API (used by matplotlib)  
RUN apt-get update && apt-get install -y python-qt4  
  
# Install R and RPY2  
RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list'  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
RUN gpg -a --export E084DAB9 | sudo apt-key add -  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install r-base r-base-dev -y  
RUN pip install rpy2==2.8.5 --ignore-installed  
RUN mkdir -p /home/$NB_USER/.ipython/profile_default/startup  
RUN echo '%load_ext rpy2.ipython' >>
/home/$NB_USER/.ipython/profile_default/startup/mymagics.ipy  
RUN chown $NB_USER:users /home/$NB_USER/.ipython -R  
  
# Install R libraries  
#RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
#RUN Rscript -e "install.packages('ggplot2')"  
#RUN Rscript -e "source('https://bioconductor.org/biocLite.R')"  
# Install the GenePattern Notebook environment  
RUN pip install nbtools genepattern-python genepattern-notebook jupyter-
wysiwyg  
  
# Enable the extension  
RUN jupyter nbextension enable \--py widgetsnbextension  
  
RUN jupyter nbextension install --py nbtools  
RUN jupyter nbextension enable \--py nbtools  
RUN jupyter serverextension enable \--py nbtools  
  
RUN jupyter nbextension install --py genepattern  
RUN jupyter nbextension enable \--py genepattern  
RUN jupyter serverextension enable \--py genepattern  
  
RUN jupyter nbextension install --py jupyter_wysiwyg  
RUN jupyter nbextension enable \--py jupyter_wysiwyg  
  
USER $NB_USER  
  

