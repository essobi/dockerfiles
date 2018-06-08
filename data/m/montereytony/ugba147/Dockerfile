#  
#  
# Build: docker build --rm --tag montereytony/ugba147 .  
# Push: docker tag my_image $DOCKER_ID_USER/my_image  
#  
# git status  
# git commit -m "comments Ubuntu and R to 3.4.2 "  
# git push  
#  
FROM jupyter/datascience-notebook  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
# Let's do updates first and install some needed libraries and utilites  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get update -y && apt-get dist-upgrade -y  
RUN apt install build-essential libssl-dev libffi-dev python-dev
lib32ncurses5-dev -y  
# gtar was used by pandoc so we need this  
RUN ln -s /bin/tar /bin/gtar  
RUN /usr/bin/apt-get install unzip  
RUN /usr/bin/wget
https://github.com/jgm/pandoc/releases/download/2.1/pandoc-2.1-1-amd64.deb  
RUN /usr/bin/dpkg -i pandoc-2.1-1-amd64.deb  
RUN rm pandoc-2.1-1-amd64.deb  
  
#  
# Upgrade R 3.4.2 now  
#  
#RUN pip uninstall ipykernel  
#RUN pip install ipykernel  
RUN conda clean -tipsy  
RUN conda update -c r r-base  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/pbdZMQ_0.3-2.tar.gz',repos=NULL)"  
RUN conda install \  
gcc_linux-64 \  
gfortran_linux-64 \  
r-essentials \  
r-htmlwidgets \  
r-gridExtra \  
r-e1071 \  
r-rgl \  
r-xlsxjars \  
r-xlsx \  
r-aer \  
r-png \  
r-rJava \  
r-devtools \  
r-digest \  
r-evaluate \  
r-memoise \  
r-withr \  
r-irdisplay \  
r-r6 \  
r-irkernel \  
r-jsonlite\  
r-lubridate\  
r-magrittr\  
r-rcpp \  
r-repr \  
r-stringi\  
r-stringr\  
r-processx\  
r-tidyverse\  
r-readr  
  
RUN conda install -c r r-igraph  
  
RUN conda install \  
ipython \  
numpy \  
pandas \  
plotnine \  
matplotlib \  
seaborn \  
phantomjs \  
statsmodels \  
statsmodels \  
python-utils  
  
RUN conda install -c https://conda.anaconda.org/amueller wordcloud  
  
# The following would not do a conda install so we compile from source  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/DRR_0.0.3.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://ftp.osuosl.org/pub/cran/src/contrib/wordcloud2_0.2.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/webshot_0.5.0.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/mclust_5.4.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/pracma_2.1.4.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/ggdendro_0.1-20.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/reshape_0.8.7.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/prettyunits_1.0.2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/progress_1.1.2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/GGally_1.3.2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/multiwayvcov_1.2.3.tar.gz',repos=NULL)"  
  
#  
# NB extensions is not working when running it in jupyterhub kubernetes so
adding this next line  
#  
RUN conda install -c conda-forge jupyter_contrib_nbextensions  
RUN jupyter nbextension install --py widgetsnbextension --sys-prefix  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/openxlsx_4.0.17.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/rio_0.5.9.tar.gz',repos=NULL)"  
  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/survey_3.33.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/coda_0.19-1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/mvtnorm_1.0-7.tar.gz',repos=NULL)"  
#RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/sfsmisc_1.1-1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/sfsmisc_1.1-2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/polycor_0.7-9.tar.gz',repos=NULL)"  
#RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/CDM_6.0-101.tar.gz',repos=NULL)"  
#RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/TAM_2.8-21.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/CDM_6.1-10.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/TAM_2.9-35.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/mitools_2.3.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/mice_2.46.0.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/mvtnorm_1.0-7.tar.gz',repos=NULL)"  
  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/GPArotation_2014.11-1.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/permute_0.9-4.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/vegan_2.4-6.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/pbivnorm_0.6.0.tar.gz',repo=NULL)"  
  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/numDeriv_2016.8-1.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/Archive/mirt/mirt_1.20.1.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/lavaan_0.5-23.1097.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/lavaan.survey_1.1.3.1.tar.gz',repo=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/sirt_2.4-20.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/miceadds_2.9-15.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/RcppRoll_0.2.2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/DEoptimR_1.0-8.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/robustbase_0.92-8.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/gower_0.1.2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/kernlab_0.9-25.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/CVST_0.2-1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/DRR_0.0.3.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.rstudio.com/src/contrib/SQUAREM_2017.10-1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/lava_1.6.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/prodlim_1.6.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/ddalpha_1.3.1.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/dimRed_0.1.0.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/ipred_0.9-6.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/recipes_0.1.2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/withr_2.1.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/caret_6.0-78.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/neuralnet_1.33.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/irlba_2.3.2.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/kknn_1.3.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/gtools_3.5.0.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/gdata_2.18.0.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/gplots_3.0.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/ROCR_1.0-7.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/MLmetrics_1.1.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/MLmetrics_1.1.1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/dummies_1.5.6.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/slam_0.1-42.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/NLP_0.1-11.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/tm_0.7-3.tar.gz',repos=NULL)"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean \  
apt autoremove  
  
#####Important########  
##To set Oracle JDK8 as default, install the "oracle-java8-set-default"
package.  
##E.g.: sudo apt install oracle-java8-set-default  
##On Ubuntu systems, oracle-java8-set-default is most probably installed  
##automatically with this package.  
######################  
#RUN apt install oracle-java8-set-default  
#RUN export LD_LIBRARY_PATH=/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server  
#RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/rJava_0.9-9.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/clipr_0.4.0.tar.gz',repos=NULL)"  
RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$JAVA_LD_LIBRARY_PATH  
RUN R CMD javareconf  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/RWekajars_3.9.2-1.tar.gz',repos=NULL)"  
#RUN conda install -c glaxosmithkline r-rwekajars  
#RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/RWekajars_3.9.2-1.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/RWeka_0.4-37.tar.gz',repos=NULL)"  
RUN Rscript -e
"install.packages('https://cran.r-project.org/src/contrib/rpart.plot_2.1.2.tar.gz',repos=NULL)"  
#  
# This should allow users to turn off extension if they do not want them.  
#  
USER jovyan  
RUN jupyter nbextensions_configurator enable  

