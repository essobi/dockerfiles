FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04  
MAINTAINER comafire <comafire@gmail.com>  
  
# Bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Common  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential vim curl wget git cmake bzip2 sudo locales unzip net-tools \  
libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
llvm \  
libfreetype6-dev libxft-dev  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common libjpeg-dev libpng-dev ncurses-dev imagemagick \  
libgraphicsmagick1-dev libzmq-dev gfortran gnuplot gnuplot-x11 libsdl2-dev \  
openssh-client htop  
  
# For Tensorflow GPU  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libcupti-dev nvidia-modprobe  
#ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH  
# Docker  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https ca-certificates  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add
-  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
RUN apt-get update && apt-get install -y --no-install-recommends \  
docker-ce  
  
# Database  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libmysqlclient-dev libpq-dev postgresql-client  
  
# Python2  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python python-dev python-pip python-virtualenv python-software-properties  
RUN pip2 install --upgrade pip  
RUN pip2 install setuptools  
  
# Python3  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python3 python3-dev python3-pip python3-virtualenv python3-software-properties  
RUN pip3 install --upgrade pip  
RUN pip3 install setuptools  
  
# JAVA http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/server-
jre-8u131-linux-x64.tar.gz  
ENV JAVA_MAJOR_VERSION 8  
ENV JAVA_UPDATE_VERSION 131  
ENV JAVA_BUILD_NUMBER 11  
ENV JAVA_TOKEN d54c1d3a095b4ff2b6607d096fa80163  
ENV JAVA_HOME /usr/local/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -sL --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/${JAVA_TOKEN}/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/local/ \  
&& ln -s $JAVA_HOME /usr/local/java \  
&& rm -rf $JAVA_HOME/man  
  
# Scala  
RUN apt-get update && apt-get install -y --no-install-recommends \  
scala  
RUN pip2 install py4j  
RUN pip3 install py4j  
  
# Julia: disable until v0.x  
#RUN add-apt-repository ppa:staticfloat/juliareleases  
#RUN add-apt-repository ppa:staticfloat/julia-deps  
#RUN apt-get update && apt-get install -y --no-install-recommends \  
#julia  
# R  
RUN apt-get update && apt-get --allow-unauthenticated install -y --no-install-
recommends \  
r-base r-base-dev  
  
# SPARK  
ENV SPARK_VERSION 2.2.0  
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-hadoop2.7  
ENV SPARK_HOME /usr/local/spark-${SPARK_VERSION}  
  
ENV PATH $PATH:${SPARK_HOME}/bin  
RUN curl -sL --retry 3 \  
"http://d3kbcqa49mib13.cloudfront.net/${SPARK_PACKAGE}.tgz" \  
| gunzip \  
| tar x -C /usr/local \  
&& mv /usr/local/$SPARK_PACKAGE $SPARK_HOME \  
&& ln -s $SPARK_HOME /usr/local/spark \  
&& chown -R root:root $SPARK_HOME  
ENV PYTHONPATH $SPARK_HOME/python/:$PYTHONPATH  
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH  
COPY spark-defaults.conf /usr/local/spark/conf/spark-defaults.conf  
  
# Jupyter Deps  
RUN apt-get update && apt-get install -y --no-install-recommends \  
texlive-xetex  
  
# Python2-Deps  
RUN pip2 install numpy scipy scikit-learn matplotlib pandas pandas_ml pandas-
datareader quandl h5py  
RUN pip2 install statsmodels imblearn awscli seaborn xgboost nbformat boto3
xlrd  
RUN pip2 install docker fabric pytest pycrypto Flask  
RUN pip2 install pymssql pymysql airflow
airflow[s3,postgres,mysql,crypto,password]  
RUN pip2 install tensorflow-gpu keras  
RUN pip2 install http://download.pytorch.org/whl/cu90/torch-0.3.1-cp27-cp27mu-
linux_x86_64.whl  
RUN pip2 install torchvision  
  
# Python3-Deps  
RUN pip3 install numpy scipy scikit-learn matplotlib pandas pandas_ml pandas-
datareader quandl h5py  
RUN pip3 install statsmodels imblearn awscli seaborn xgboost nbformat boto3
xlrd  
RUN pip3 install docker fabric pytest pycrypto Flask  
RUN pip3 install pymssql pymysql airflow
airflow[s3,postgres,mysql,crypto,password]  
RUN pip3 install tensorflow-gpu keras  
RUN pip3 install
http://download.pytorch.org/whl/cu90/torch-0.3.1-cp35-cp35m-linux_x86_64.whl  
RUN pip3 install torchvision  
  
# Jupyter  
RUN pip3 install jupyter  
# Jupyter extensions  
RUN pip3 install jupyter_contrib_nbextensions  
RUN pip3 install jupyter_nbextensions_configurator  
RUN pip3 install yapf  
#RUN pip3 install
https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0/snapshots/dev1/toree-
pip/toree-0.2.0.dev1.tar.gz  
RUN pip3 install toree  
# TOREE python, R is not stable  
#RUN jupyter toree install --interpreters=Scala,PySpark,SparkR,SQL
--spark_home=$SPARK_HOME --user  
RUN jupyter toree install --interpreters=Scala --spark_home=$SPARK_HOME
\--user  
RUN pip3 install nbimporter jdc jupyter_kernel_gateway  
  
# Jupyter python2 kernel  
RUN python2 -m pip install ipykernel  
RUN python2 -m ipykernel install --user  
RUN pip2 install nbimporter jdc jupyter_kernel_gateway  
  
# Jupyter Julia Kernel  
#RUN julia -e 'Pkg.add("IJulia")'  
# Jupyter R kernel  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libcurl4-gnutls-dev libxml2-dev libssl-dev  
RUN R -e "install.packages(c('curl', 'repr', 'httr'),
repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages(c('pbdZMQ', 'devtools', 'IRdisplay', 'evaluate',
'crayon', 'uuid', 'digest'), repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages(c('SparkR'), repos='http://cran.rstudio.com/')"  
RUN R -e "devtools::install_github('IRkernel/IRkernel')"  
RUN R -e "IRkernel::installspec()"  
  
# Env  
VOLUME /root/volume  
  
EXPOSE 8888 8088  
WORKDIR /root/volume  
CMD ["./run_jupyter.sh"]  
  

