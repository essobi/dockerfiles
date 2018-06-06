FROM rpy2/rpy2:devel  
  
MAINTAINER Laurent Gautier <lgautier@gmail.com>  
  
USER root  
  
RUN \  
apt-get update -qq && \  
apt-get install -y \  
ed \  
git \  
llvm-3.7-tools \  
libcairo-dev \  
libedit-dev \  
lsb-release \  
llvm-3.7 \  
scala \  
wget &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
wget --progress=bar
http://mirrors.ocf.berkeley.edu/apache/spark/spark-2.0.0/spark-2.0.0-bin-
hadoop2.7.tgz && \  
tar -xzf spark-2.0.0-bin-hadoop2.7.tgz && \  
mv spark-2.0.0-bin-hadoop2.7 /opt/ && \  
rm spark-2.0.0-bin-hadoop2.7.tgz  
  
  
# Add CRAN repository  
#RUN \  
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \  
# echo "deb http://cran.cnr.Berkeley.edu/bin/linux/ubuntu `lsb_release -a |
gre#p Codename | awk '{print $2}'`/" >> /etc/apt/sources.list  
  
RUN \  
pip3 --no-cache-dir install wheel --upgrade && \  
pip3 --no-cache-dir install sqlalchemy && \  
rm -rf /root/.cache && \  
wget https://github.com/numba/llvmlite/archive/v0.12.1.zip && \  
unzip v0.12.1.zip && \  
cd llvmlite-0.12.1 && \  
LLVM_CONFIG=`which llvm-config-3.7` python3 setup.py install && \  
cd .. && rm -rf llvmlite-0.12.1 && rm v0.12.1.zip && \  
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
R -e 'install.packages(sub("(.+)\\\\n","\\1", scan("rpacks.txt",
"character")), repos="http://cran.cnr.Berkeley.edu")' && \  
rm rpacks.txt  
  
#COPY notebooks/finefoods.db /notebooks/  
  
COPY finefoods_to_sqlite.py /opt/data/finefoods_to_sqlite.py  
  
RUN \  
cd /opt/data && \  
wget -q --show-progress --progress=bar:force \  
http://snap.stanford.edu/data/finefoods.txt.gz && \  
python3 finefoods_to_sqlite.py && \  
rm finefoods.txt.gz  
  
ENV NB_USER jupyteruser  
ENV SPARK_HOME /opt/spark-2.0.0-bin-hadoop2.7  
  
WORKDIR /home/$NB_USER/work  
  
RUN pip3 --no-cache install notedown && \  
rm -rf /root/.cache  
  
USER $NB_USER  
RUN mkdir -p /home/$NB_USER/work  
COPY notebooks/slides.ipynb /home/$NB_USER/work  
  
CMD jupyter notebook --no-browser  

