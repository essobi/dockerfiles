FROM jupyter/datascience-notebook:400c69639ea5  
  
USER root  
  
ADD https://raw.githubusercontent.com/hammerlab/immune-infiltrate-
explorations/master/model-single-origin-samples/biokepi/conda_requirements.txt
/home/jovyan/conda_requirements.txt  
ADD https://raw.githubusercontent.com/hammerlab/immune-infiltrate-
explorations/master/model-single-origin-samples/biokepi/pip_requirements.txt
/home/jovyan/pip_requirements.txt  
RUN chown jovyan:users /home/jovyan/conda_requirements.txt  
RUN chown jovyan:users /home/jovyan/pip_requirements.txt  
  
USER jovyan  
  
COPY install_Cibersort_dependencies.R
/home/jovyan/install_Cibersort_dependencies.R  
COPY runRserve.R /home/jovyan/runRserve.R  
  
RUN conda install --file=/home/jovyan/conda_requirements.txt  
  
RUN pip install -r /home/jovyan/pip_requirements.txt  
  
USER root  
  
# set up jdk (to run cibersort)  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#run  
RUN apt-get update -y && apt-get install -y openjdk-8-jdk  
ENV JAVA_HOME='/usr/lib/jvm/java-8-openjdk-amd64'  
RUN javac -version # validates that installed  
  
# set up R dependencies for Cibersort  
ENV LD_LIBRARY_PATH="/opt/conda/lib/R/lib:/opt/conda/lib:${LD_LIBRARY_PATH}"  
RUN Rscript /home/jovyan/install_Cibersort_dependencies.R  
# Rserve need to install from source to run from command line  
# RUN wget -P /home/jovyan/
https://cran.r-project.org/src/contrib/Rserve_1.7-3.tar.gz  
# RUN R CMD INSTALL /home/jovyan/Rserve_1.7-3.tar.gz  
# install imagemagick  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#run  
RUN apt-get update && apt-get install -y \  
wget \  
imagemagick \  
parallel \  
tzdata \  
libicu-dev;  
  
# need tzdata for timezone data folder /usr/share/zoneinfo to be populated.
required to have R parse datetimes in csvs properly. confirm installed by
running `str(OlsonNames())` in R -- should not be empty  
## set up R dependencies for Rinfino  
RUN ln -s /bin/tar /bin/gtar; # necessary for bioclite and
devtools::install_github, at least for grimbough/biomaRt -- calls out to gtar
for some reason  
  
# catches a warning like "couldn't install package" and makes it an error  
RUN Rscript -e "install.packages(c('Rcpp'), repo='http://cran.rstudio.com')";  
RUN Rscript -e "install.packages(c('stringi', 'stringr'),
repos='http://cran.rstudio.com/')"; # requires libicu-dev to be installed  
  
# to install R packages, first check if they're listed here:
https://docs.anaconda.com/anaconda/packages/r-language-pkg-docs  
RUN conda install -c r --quiet --yes \  
'r-essentials' \  
'r-rserve' \  
'r-dplyr' \  
'r-e1071' \  
'r-glue' \  
'r-lubridate' \  
'r-purrr' \  
'r-stringr' \  
'r-tibble' \  
'r-readr' \  
'r-tidyr' \  
'r-magrittr' \  
'r-rmarkdown' \  
'r-reticulate' \  
'r-readxl' \  
'r-testthat' \  
'r-rcolorbrewer' \  
'r-formatr';  
  
RUN conda install -c r --quiet --yes 'r-xml';  
RUN conda install --quiet --yes gxx_linux-64; # needed for purrrlyr
(https://github.com/RcppCore/Rcpp/issues/770)  
RUN conda install --quiet --yes gcc_linux-64 gfortran_linux-64; # needed for
statmod ("/opt/conda/bin/x86_64-conda_cos6-linux-gnu-gfortran: Command not
found"): see https://conda.io/docs/di-guide/tasks/build-packages/compiler-
tools.html  
RUN Rscript -e "withCallingHandlers(install.packages(c( \  
'estimate', \  
'purrrlyr', \  
'txtplot', \  
'statmod'), repos=c('http://cran.rstudio.com', 'http://r-forge.r-project.org',
'http://www.bioconductor.org/packages/release/bioc')), warning = function(w)
stop(w))";  
  
RUN Rscript -e "source('https://bioconductor.org/biocLite.R');
biocLite(c('grimbough/biomaRt', \  
'sva', \  
'tximport', \  
'Rsubread', \  
'rhdf5', \  
'edgeR', \  
'limma'))";  
  
#RUN Rscript -e "library(devtools);
devtools::install_github('hammerlab/rinfino', dependencies=T)";  
# dev version instead:  
RUN Rscript -e "library(devtools);
devtools::install_github('maximz/rinfino@ux_changes', dependencies=T)";  
  
# set up infino python package  
# see https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support  
RUN pip install -e
git+https://github.com/hammerlab/infino.git@develop#egg=infino  
  
USER jovyan  
  
# set up dependencies  
RUN pyensembl install --release 79 --species homo_sapiens # this requires a
lot of memory (if we see Killed, it's an out-of-memory error that requires
allocating more memory to the docker machine or VM)  
RUN pip install git+git://github.com/jburos/nbutils  
RUN pip install jupyter_contrib_nbextensions==0.4.0  
RUN pip install --upgrade jupyter-core # necessary for next line  
RUN jupyter contrib nbextension install --user # seems to require jupyter-
core>=4.4.0  
  
# enable useful nbextensions  
RUN jupyter nbextension enable code_prettify/code_prettify  
RUN jupyter nbextension enable collapsible_headings/main  
RUN jupyter nbextension enable freeze/main  
RUN jupyter nbextension enable notify/notify  
RUN jupyter nbextension enable toc2/main  
RUN jupyter nbextension enable varInspector/main  
RUN jupyter nbextension enable execute_time/ExecuteTime  
RUN jupyter nbextension enable init_cell/main  
RUN jupyter nbextension enable table_beautifier/main  
RUN jupyter nbextension enable python-markdown/main  
  
# this next line is needed for the code prettify extension  
RUN pip install yapf  
  
# disable auto running initialization cells when you load a notebook. so that
reloads aren't annoying  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64  
RUN chmod +x jq-linux64  
RUN cp /home/jovyan/.jupyter/nbconfig/notebook.json
/home/jovyan/notebook.json.bak  
RUN cat /home/jovyan/notebook.json.bak | ./jq-linux64 '. + {"init_cell":
{"run_on_kernel_ready": false}}' >
/home/jovyan/.jupyter/nbconfig/notebook.json  
  
# install cmdstan (run make with 4 cores)  
RUN wget https://github.com/stan-
dev/cmdstan/releases/download/v2.16.0/cmdstan-2.16.0.tar.gz  
RUN tar -zxvf cmdstan-2.16.0.tar.gz  
# sometimes the directory name is cmdstan-2.16.0; other times it's just
cmdstan-.  
#RUN make build -C /home/jovyan/cmdstan-2.16.0  
# extract directory name: https://unix.stackexchange.com/a/246807/6448  
RUN mv "/home/jovyan/`tar -tzf cmdstan-2.16.0.tar.gz | head -1 | cut -f1
-d"/"`" "/home/jovyan/cmdstan"  
RUN make build -C /home/jovyan/cmdstan  
ENV PATH="/home/jovyan/cmdstan/bin:${PATH}"  
# below needed to fix cython behavior (for stan especially)  
# can test behavior with: python -c 'import
sklearn.linear_model.tests.test_randomized_l1'  
# (https://github.com/BVLC/caffe/issues/3884)  
RUN conda install --yes mkl mkl-service  
RUN python -c 'import sklearn.linear_model.tests.test_randomized_l1'  
  
EXPOSE 8888  
#CMD ["/bin/bash"]  
# CMD ["start-notebook.sh", "--NotebookApp.token=''"]  
# start Rserv in daemon mode for Cibersort  
CMD Rscript /home/jovyan/runRserve.R && start-notebook.sh
--NotebookApp.token=''

