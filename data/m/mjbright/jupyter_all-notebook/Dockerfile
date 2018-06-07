# Docker demo image, as used on try.jupyter.org and tmpnb.org  
FROM jupyter/datascience-notebook  
  
MAINTAINER Michael Bright <github.com@mjbright.net>  
  
#USER root  
RUN apt-get update -y  
ENV PATH $CONDA_DIR/bin:$PATH  
  
# Ruby dependencies  
RUN apt-get install -y --no-install-recommends ruby ruby-dev libtool autoconf
automake gnuplot-nox libsqlite3-dev libatlas-base-dev libgsl0-dev && apt-get
clean && ln -s /usr/bin/libtoolize /usr/bin/libtool  
RUN apt-get install -y --no-install-recommends libmagick++-dev imagemagick  
RUN gem install --no-rdoc --no-ri sciruby-full  
  
RUN groupadd -g 1000 docker && \  
usermod -a -G docker jovyan  
  
# Setup sudoers without password:  
ADD sudoers /etc/sudoers  
  
# Needed so notebooks can write to mounted work volume:  
RUN [ ! -d /home/jovyan/work ] && mkdir /home/jovyan/work; RET=0  
RUN chown jovyan /home/jovyan/work && chmod a+w /home/jovyan/work  
  
ADD docker /home/jovyan/work/docker  
  
# Install setup ssh:  
RUN apt-get install -y openssh-client  
RUN mkdir -p /home/jovyan/.ssh  
  
#### # Install setup xdot: (for graphical display of GraphViz)  
#### RUN apt-get install -y xdot  
RUN mkdir -p /home/jovyan/src/git  
RUN chown -R jovyan /home/jovyan/src/git && chmod -R o+rwx
/home/jovyan/src/git  
RUN ls -altrd /home/jovyan/src/git  
  
# Install nbgrader extension:  
USER root  
RUN apt-get install -y pandoc  
  
USER jovyan  
#RUN cd /home/jovyan/src/git  
#RUN git clone https://github.com/jupyter/nbgrader  
#RUN pwd  
RUN cd /home/jovyan/src/git && \  
git clone https://github.com/jupyter/nbgrader && \  
cd /home/jovyan/src/git/nbgrader && \  
python setup.py install  
  
ENV PATH /home/jovyan/.local/bin/:$PATH  
  
RUN nbgrader extension install --user --symlink && \  
nbgrader extension activate  
  
# Featured notebooks  
RUN git clone \--depth 1 https://github.com/jvns/pandas-cookbook.git
/home/jovyan/featured/pandas-cookbook/  
  
# Convert notebooks to the current format  
RUN find . -name '*.ipynb' -exec ipython nbconvert --to notebook {} --output
{} \; ; echo  
RUN find . -name '*.ipynb' -exec ipython trust {} \; ; echo  
  
USER root  
  
  
# ---- Taken from all-spark Dockerfile
-----------------------------------------------  
# Spark dependencies  
ENV APACHE_SPARK_VERSION 1.4.1  
RUN apt-get install -y --no-install-recommends openjdk-7-jre-headless && \  
apt-get clean  
RUN wget -qO -
http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-
hadoop2.6.tgz | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6 spark  
  
# Mesos dependencies  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
DISTRO=debian && \  
CODENAME=wheezy && \  
echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get -y update && \  
apt-get --no-install-recommends -y --force-yes install
mesos=0.22.1-1.0.debian78 && \  
apt-get clean  
  
# Scala Spark kernel (build and cleanup)  
RUN cd /tmp && \  
echo deb http://dl.bintray.com/sbt/debian / > /etc/apt/sources.list.d/sbt.list
&& \  
apt-get update && \  
git clone https://github.com/ibm-et/spark-kernel.git && \  
apt-get install -yq --force-yes --no-install-recommends sbt && \  
cd spark-kernel && \  
sbt compile -Xms1024M \  
-Xmx2048M \  
-Xss1M \  
-XX:+CMSClassUnloadingEnabled \  
-XX:MaxPermSize=1024M && \  
sbt pack && \  
mv kernel/target/pack /opt/sparkkernel && \  
chmod +x /opt/sparkkernel && \  
rm -rf ~/.ivy2 && \  
rm -rf ~/.sbt && \  
rm -rf /tmp/spark-kernel && \  
apt-get remove -y sbt && \  
apt-get clean  
  
# Spark and Mesos pointers  
ENV SPARK_HOME /usr/local/spark  
ENV R_LIBS_USER $SPARK_HOME/R/lib  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip  
ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so  
  
USER jovyan  
  
# Install Python 3 packages  
RUN conda install --yes \  
'ipywidgets=4.0*' \  
'pandas=0.16*' \  
'matplotlib=1.4*' \  
'scipy=0.15*' \  
'seaborn=0.6*' \  
'scikit-learn=0.16*' \  
&& conda clean -yt  
  
# Install Python 2 packages  
# RUN python2 --version  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ 'ipython=4.0*'  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ 'ipywidgets=4.0*'  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ 'pandas=0.16*'  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ 'matplotlib=1.4*'  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ 'scipy=0.15*'  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ 'seaborn=0.6*'  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ 'scikit-
learn=0.16*'  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \ pyzmq  
# RUN conda clean -yt  
#  
# RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \  
# 'ipython=4.0*' \  
# 'ipywidgets=4.0*' \  
# 'pandas=0.16*' \  
# 'matplotlib=1.4*' \  
# 'scipy=0.15*' \  
# 'seaborn=0.6*' \  
# 'scikit-learn=0.16*' \  
# pyzmq \  
# && conda clean -yt  
# R packages  
RUN conda config --add channels r  
RUN conda install --yes \  
'r-base=3.2*' \  
'r-irkernel=0.4*' \  
'r-ggplot2=1.0*' \  
'r-rcurl=1.95*' && conda clean -yt  
  
# Scala Spark kernel spec  
RUN mkdir -p /opt/conda/share/jupyter/kernels/scala  
COPY all-spark_kernel.json /opt/conda/share/jupyter/kernels/scala/  
  
USER root  
  
# Install Python 2 kernel spec globally to avoid permission problems when
NB_UID  
# switching at runtime.  
RUN $CONDA_DIR/envs/python2/bin/python \  
$CONDA_DIR/envs/python2/bin/ipython \  
kernelspec install-self  
  
USER jovyan  
  
#[datascience-notebook]# Install IJulia and Julia packages:  
RUN julia -e 'Pkg.add("IJulia")'  
RUN julia -e 'Pkg.add("Interact")'  
RUN julia -e 'Pkg.add("Gadfly")' && julia -e 'Pkg.add("RDatasets")'  
RUN pip install Julia  
  
# IRuby  
RUN iruby register  
  
# Install bash_kernel:  
# Make sure not to create a cache dir else NB_UID switching  
# will hit issues.  
RUN pip install --no-cache-dir bash_kernel && \  
python -m bash_kernel.install  
  
# Install RISE (LIVE Reveal) extension:  
RUN cd /home/jovyan && \  
cd /home/jovyan/src/git && \  
git clone https://github.com/damianavila/RISE
/home/jovyan/src/git/damianvila.RISE && \  
cd /home/jovyan/src/git/damianvila.RISE && \  
python setup.py install  
  
USER jovyan  
  
# Install hide_code extension:  
# - original not Python3 - git clone https://github.com/kirbs-/hide_code && \  
RUN cd /home/jovyan/src/git && \  
git clone https://github.com/mjbright/hide_code && \  
cd /home/jovyan/src/git/hide_code && \  
python setup.py install  
  
USER root  
  
ENV JUPYTER_CONFIG_DIR jupyter --config-dir  
  
# Removed:  
#ADD custom.css $JUPYTER_CONFIG_DIR/  

