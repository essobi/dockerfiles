FROM ubuntu:16.04  
MAINTAINER comafire <comafire@gmail.com>  
  
# Bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Lang  
RUN apt-get update && apt-get install -y --no-install-recommends \  
locales language-pack-ko  
RUN echo "ko_KR.UTF-8 UTF-8" > /etc/locale.gen && locale-gen  
ENV LC_ALL ko_KR.UTF-8  
ENV LANG ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
# Common  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential vim curl wget git cmake bzip2 sudo unzip net-tools \  
libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
llvm \  
libfreetype6-dev libxft-dev  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common libjpeg-dev libpng-dev ncurses-dev imagemagick \  
libgraphicsmagick1-dev libzmq-dev gfortran gnuplot gnuplot-x11 libsdl2-dev \  
openssh-client htop  
  
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
ENV JAVA_UPDATE_VERSION 172  
ENV JAVA_BUILD_NUMBER 11  
ENV JAVA_TOKEN a58eab1ec242421181065cdc37240b08  
ENV JAVA_HOME /usr/local/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -sL --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/${JAVA_TOKEN}/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip | tar x -C /usr/local/ \  
&& ln -s $JAVA_HOME /usr/local/java \  
&& rm -rf $JAVA_HOME/man  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
maven  
  
# Scala  
ENV SCALA_VERSION 2.11.11  
ENV SCALA_HOME /usr/local/scala-${SCALA_VERSION}  
  
ENV PATH $PATH:$SCALA_HOME/bin  
RUN curl -sL --retry 3 --insecure \  
"https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz"
\  
| gunzip | tar x -C /usr/local/ \  
&& ln -s $SCALA_HOME /usr/local/scala  
  
# Julia  
# install Julia packages in /opt/julia instead of $HOME  
ENV JULIA_PKGDIR=/opt/julia  
ENV JULIA_VERSION=0.6.2  
RUN mkdir /opt/julia-${JULIA_VERSION} && \  
cd /tmp && \  
wget -q https://julialang-s3.julialang.org/bin/linux/x64/`echo
${JULIA_VERSION} | cut -d. -f 1,2`/julia-${JULIA_VERSION}-linux-x86_64.tar.gz
&& \  
echo "dc6ec0b13551ce78083a5849268b20684421d46a7ec46b17ec1fab88a5078580
*julia-${JULIA_VERSION}-linux-x86_64.tar.gz" | sha256sum -c - && \  
tar xzf julia-${JULIA_VERSION}-linux-x86_64.tar.gz -C
/opt/julia-${JULIA_VERSION} \--strip-components=1 && \  
rm /tmp/julia-${JULIA_VERSION}-linux-x86_64.tar.gz  
RUN ln -fs /opt/julia-*/bin/julia /usr/local/bin/julia  
  
# R  
RUN apt-get update && apt-get --allow-unauthenticated install -y --no-install-
recommends \  
r-base r-base-dev  
  
# Go  
ENV GO_VERSION 1.9.5  
ENV GO_OS linux  
ENV GO_ARCH amd64  
RUN wget https://dl.google.com/go/go$GO_VERSION.$GO_OS-$GO_ARCH.tar.gz  
RUN tar -C /usr/local/ -xzf go$GO_VERSION.$GO_OS-$GO_ARCH.tar.gz  
RUN mv /usr/local/go /usr/local/go-$GO_VERSION  
RUN ln -s /usr/local/go-$GO_VERSION /usr/local/go  
ENV PATH $PATH:/usr/local/go/bin  
  
# SPARK  
ENV SPARK_VERSION 2.3.0  
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-hadoop2.7  
ENV SPARK_HOME /usr/local/spark-${SPARK_VERSION}  
ENV PY4J_VERSION 0.10.6  
ENV PATH $PATH:${SPARK_HOME}/bin  
RUN curl -sL --retry 3 \  
"http://apache.mirror.cdnetworks.com/spark/spark-${SPARK_VERSION}/${SPARK_PACKAGE}.tgz"
\  
| gunzip | tar x -C /usr/local \  
&& mv /usr/local/$SPARK_PACKAGE $SPARK_HOME \  
&& ln -s $SPARK_HOME /usr/local/spark \  
&& chown -R root:root $SPARK_HOME  
ENV PYTHONPATH $SPARK_HOME/python/:$PYTHONPATH  
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-$PY4J_VERSION-src.zip:$PYTHONPATH  
  
RUN pip2 install py4j==$PY4J_VERSION  
RUN pip3 install py4j==$PY4J_VERSION  
  
# Jupyter Deps  
RUN apt-get update && apt-get install -y --no-install-recommends \  
texlive-xetex  
  
# Python2 Deps  
RUN pip2 install numpy scipy scikit-learn matplotlib pandas pandas_ml pandas-
datareader quandl h5py  
RUN pip2 install statsmodels imblearn awscli seaborn xgboost nbformat boto3
xlrd pyarrow  
RUN pip2 install docker fabric pytest pycrypto Flask  
RUN pip2 install pymssql pymysql airflow
airflow[s3,postgres,mysql,crypto,password]  
RUN pip2 install tensorflow keras  
RUN pip2 install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp27-cp27mu-
linux_x86_64.whl  
RUN pip2 install torchvision  
  
# Python3 Deps  
RUN pip3 install numpy scipy sklearn matplotlib pandas pandas_ml pandas-
datareader quandl h5py  
RUN pip3 install statsmodels imblearn awscli seaborn xgboost nbformat boto3
xlrd pyarrow  
RUN pip3 install docker fabric pytest pycrypto Flask  
RUN pip3 install pymssql pymysql airflow
airflow[s3,postgres,mysql,crypto,password]  
RUN pip3 install tensorflow keras  
RUN pip3 install
http://download.pytorch.org/whl/cpu/torch-0.4.0-cp35-cp35m-linux_x86_64.whl  
RUN pip3 install torchvision  
  
# Jupyter  
RUN pip3 install jupyter  
# Jupyter extensions  
RUN pip3 install jupyter_contrib_nbextensions  
RUN pip3 install jupyter_nbextensions_configurator  
RUN pip3 install yapf  
RUN pip3 install nbimporter jdc jupyter_kernel_gateway  
  
# Jupyter Python2 kernel  
RUN python2 -m pip install ipykernel  
RUN python2 -m ipykernel install --user  
  
# Jupyter Python3 kernel  
RUN python3 -m pip install ipykernel  
RUN python3 -m ipykernel install --user  
  
# Jupyter Scala  
RUN git clone https://github.com/alexarchambault/jupyter-scala.git;cd jupyter-
scala;./jupyter-scala  
  
# Jupyter Julia Kernel  
RUN julia -e 'Pkg.init()' && \  
julia -e 'Pkg.update()' && \  
julia -e 'Pkg.add("Gadfly")' && \  
julia -e 'Pkg.add("RDatasets")' && \  
julia -e 'Pkg.add("Spark.jl")' && \  
julia -e 'Pkg.add("IJulia")' && \  
# Precompile Julia packages  
julia -e 'using IJulia'  
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
  
# Go Kernel  
ENV GOPATH $HOME/go  
ENV LGOPATH $HOME/lgo  
ENV PATH $PATH:$GOPATH/bin:$LGOPATH/bin  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libzmq3-dev  
RUN go get github.com/yunabe/lgo/cmd/lgo && go get -d
github.com/yunabe/lgo/cmd/lgo-internal  
RUN lgo install  
RUN python3 $(go env GOPATH)/src/github.com/yunabe/lgo/bin/install_kernel  
  
# Env  
VOLUME /root/volume  
  
EXPOSE 8888 8088  
WORKDIR /root/volume  
CMD ["./run_jupyter.sh"]  
  

