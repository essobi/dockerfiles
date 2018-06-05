FROM ubuntu:16.04  
MAINTAINER ajay@deonarine.com  
  
RUN apt-get upgrade -y && apt-get dist-upgrade  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
build-essential \  
gdebi-core \  
libcurl4-openssl-dev \  
libssl-dev \  
libssh2-1-dev \  
#nodejs-legacy \  
#npm \  
python3-pip \  
r-base \  
software-properties-common \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN add-apt-repository ppa:staticfloat/juliareleases  
RUN add-apt-repository ppa:staticfloat/julia-deps  
  
##Add new cran repo  
RUN echo 'deb https://cloud.r-project.org/bin/linux/ubuntu xenial/' >>
/etc/apt/sources.list  
  
##Add Key  
RUN gpg --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys E084DAB9  
RUN gpg -a \--export E084DAB9 | apt-key add -  
  
##Upgrade R  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
julia \  
&& rm -rf /var/lib/apt/lists/*  
  
##Install R packages  
RUN su - -c "R -e \"install.packages(c( \  
'curl', \  
'data.table', \  
'DBI', \  
'dplyr', \  
'devtools', \  
'doMC', \  
'foreach', \  
'ggplot2', \  
'ggvis', \  
'httr', \  
'jsonlite', \  
'lubridate', \  
'rbokeh', \  
'readr', \  
'Rcpp', \  
'stringr', \  
'tidyr', \  
'xml2' \  
), repos = 'http://cloud.r-project.org/')\""  
  
##Install XGBoost - R  
RUN R -e "install.packages('xgboost', repos='http://dmlc.ml/drat/',
type='source')"  
  
RUN pip3 install --upgrade pip  
RUN pip3 install \  
flask \  
jupyter \  
keras \  
numpy \  
pandas \  
scipy \  
scikit-learn  
  
##Install Tensorflow  
ENV TF_BINARY_URL
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl  
RUN pip3 install --upgrade $TF_BINARY_URL  
  
##Install XGBoost - python  
RUN cd /tmp && \  
git clone --recursive https://github.com/dmlc/xgboost && \  
cd xgboost && \  
make -j4 &&\  
cd python-package && \  
python3 setup.py install  
  
##Install R Kernel  
RUN R -e "install.packages(c( \  
'repr', \  
'IRdisplay', \  
'evaluate', \  
'crayon', \  
'pbdZMQ', \  
'uuid', \  
'digest' \  
), repos = 'http://cloud.r-project.org/') "  
  
#RUN su - -c "R -e \"devtools::install_github('IRkernel/IRkernel')\""  
#RUN su - -c "R -e \"IRkernel::installspec(user = FALSE)\""  
  
RUN R -e "devtools::install_github('IRkernel/IRkernel')"  
RUN R -e "IRkernel::installspec(user = FALSE)"  
  
#Install Tensorflow Package  
ENV TENSORFLOW_PYTHON_VERSION 3  
RUN R -e "devtools::install_github('rstudio/tensorflow')"  
  
##Install Julia Kernel  
RUN julia -e "Pkg.add(\"IJulia\")"  
RUN julia -e "Pkg.update()"  
  
EXPOSE 8888  
  
RUN pip3 list  
RUN cat /etc/debian_version  
RUN cat /etc/issue.net  
  
WORKDIR /home/work

