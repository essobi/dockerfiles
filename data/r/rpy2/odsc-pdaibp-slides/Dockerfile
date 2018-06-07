FROM ubuntu:16.04  
MAINTAINER Laurent Gautier <lgautier@gmail.com>  
  
RUN \  
apt-get update -qq && \  
apt-get install -y \  
ed \  
git \  
llvm-3.7-tools \  
libcairo-dev \  
libedit-dev \  
lsb-release \  
python3 \  
python3-pip \  
r-base \  
r-base-dev \  
llvm-3.7 \  
scala \  
wget &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
wget --progress=bar
http://mirrors.ocf.berkeley.edu/apache/spark/spark-1.6.1/spark-1.6.1-bin-
hadoop2.6.tgz && \  
tar -xzf spark-1.6.1-bin-hadoop2.6.tgz && \  
mv spark-1.6.1-bin-hadoop2.6 /opt/ && \  
rm spark-1.6.1-bin-hadoop2.6.tgz  
  
# Add CRAN repository  
#RUN \  
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \  
# echo "deb http://cran.cnr.Berkeley.edu/bin/linux/ubuntu `lsb_release -a |
gre#p Codename | awk '{print $2}'`/" >> /etc/apt/sources.list  
RUN \  
pip3 --no-cache-dir install pip --upgrade && \  
pip3 --no-cache-dir install setuptools --upgrade && \  
pip3 --no-cache-dir install wheel --upgrade && \  
pip3 --no-cache-dir install numpy pandas sphinx jinja2 jupyter notebook && \  
pip3 --no-cache-dir install bokeh && \  
pip3 --no-cache-dir install sqlalchemy && \  
rm -rf /root/.cache && \  
wget https://github.com/numba/llvmlite/archive/v0.10.0.zip && \  
unzip v0.10.0.zip && \  
cd llvmlite-0.10.0 && \  
LLVM_CONFIG=`which llvm-config-3.7` python3 setup.py install && \  
cd .. && rm -rf llvmite-0.10.0 && rm v0.10.0.zip && \  
pip3 --no-cache install numba && \  
pip3 --no-cache install findspark && \  
rm -rf /root/.cache  
  
RUN \  
echo "broom\n\  
dplyr\n\  
hexbin\n\  
glmnet\n\  
ggplot2\n\  
gridExtra\n\  
lme4\n\  
plotly\n\  
RSQLite\n\  
svglite\n\  
tidyr" > rpacks.txt && \  
R -e 'install.packages(sub("(.+)\\\\\\\n","\\\1", scan("rpacks.txt",
"character")), repos="http://cran.cnr.Berkeley.edu")' && \  
rm rpacks.txt  
  
# Run dev version of rpy2  
RUN \  
pip3 --no-cache-dir install \  
https://bitbucket.org/rpy2/rpy2/get/RELEASE_2_8_0.tar.gz && \  
rm -rf /root/.cache  
  
COPY finefoods_to_sqlite.py /opt/data/finefoods_to_sqlite.py  
  
RUN \  
cd /opt/data && \  
wget -q --show-progress --progress=bar:force \  
http://snap.stanford.edu/data/finefoods.txt.gz && \  
python3 finefoods_to_sqlite.py && \  
rm finefoods.txt.gz  
  
ENV SHELL /bin/bash  
ENV NB_USER jupyteruser  
ENV NB_UID 1000  
ENV SPARK_HOME /opt/spark-1.6.1-bin-hadoop2.6  
# Create user  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER  
  
USER $NB_USER  
  
# Setup home directory and notebook config  
RUN mkdir /home/$NB_USER/work && \  
mkdir /home/$NB_USER/.jupyter && \  
mkdir /home/$NB_USER/.local && \  
echo "cacert=/etc/ssl/certs/ca-certificates.crt" > /home/$NB_USER/.curlrc && \  
echo "c.NotebookApp.ip = '*'" >>
/home/$NB_USER/.jupyter/jupyter_notebook_config.py  
  
USER root  
  
WORKDIR /home/$NB_USER/work  
  
EXPOSE 8888  
USER $NB_USER  
COPY pragmatic_polyglot.ipynb /home/$NB_USER/work  
  
CMD jupyter notebook --no-browser

