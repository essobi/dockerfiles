FROM antergos/makepkg:latest  
  
LABEL maintainer="Mateusz Kubuszok <mateusz.kubuszok@gmail.com>"  
  
# Basic preparations (jupyter user and aliases)  
USER root  
RUN pacman -Sy --noconfirm yaourt && \  
pacman -Sy --noconfirm sudo && \  
chmod 640 /etc/sudoers && echo '%wheel ALL=(ALL) NOPASSWD: ALL' >>
/etc/sudoers && chmod 440 /etc/sudoers && useradd -m -p123123 -G wheel jupyter  
WORKDIR /tmp  
ENV NB_USER jupyter  
ENV NB_HOME /home/$NB_USER  
COPY aliases/* /usr/local/bin/  
  
# Jupyter Lab  
RUN yaourt-install \  
ipython \  
ipython2 \  
python-ipykernel \  
python-matplotlib \  
python-numpy \  
python2-ipykernel \  
python2-numpy \  
python2-scipy \  
jupyterlab-git && \  
as-user python -m ipykernel install --user && \  
as-user python2 -m ipykernel install --user && \  
yaourt-clean  
  
# Spark and Apache Toree (Scala)  
ENV APACHE_SPARK_VERSION 2.3.0  
ENV HADOOP_VERSION 2.7  
RUN yaourt-install \  
jdk8-openjdk \  
jdk9-openjdk \  
python-pip && \  
pip install --upgrade pip && \  
wget -q
http://apache.claz.org/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz && \  
echo
"258683885383480BA01485D6C6F7DC7CFD559C1584D6CEB7A3BBCF484287F7F57272278568F16227BE46B4F92591768BA3D164420D87014A136BF66280508B46
*spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c
- && \  
tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /opt
--owner root --group root --no-same-owner && \  
ln -s /opt/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
/opt/spark && \  
yaourt-clean spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz  
RUN archlinux-java set java-8-openjdk && \  
as-user gpg --recv-keys D10295D0D6EF55AD && \  
yaourt-install \  
mesos && \  
yaourt-clean $NB_HOME/.m2  
ENV SPARK_HOME /opt/spark  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.6-src.zip  
ENV MESOS_NATIVE_LIBRARY /usr/lib/libmesos.so  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info  
RUN pip install --no-cache-dir
https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0-incubating-
rc3/toree-pip/toree-0.2.0.tar.gz && \  
jupyter toree install --spark_home=/opt/spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION} && \  
yaourt-clean  
  
# Cling (C++)  
RUN yaourt-install \  
cling-jupyter-git && \  
yaourt-clean  
  
# Haskell  
RUN yaourt-install \  
stack && \  
as-user stack install ihaskell && \  
as-user $NB_HOME/.local/bin/ihaskell install --stack && \  
yaourt-clean $NB_HOME/.stack/{indices,programs}  
  
# Java and Clojure  
RUN yaourt-install \  
leiningen && \  
archlinux-java set java-9-openjdk && \  
yaourt-install \  
ijava-git && \  
archlinux-java set java-8-openjdk && \  
git clone https://github.com/clojupyter/clojupyter /tmp/clojupyter && \  
cd /tmp/clojupyter && \  
make && \  
as-user make install && \  
yaourt-clean $NB_HOME/.m2  
  
# JavaScript  
RUN yaourt-install \  
ijavascript && \  
as-user ijs --ijs-install-kernel && \  
yaourt-clean $NB_HOME/{.node-gyp,.npm}  
  
# Ruby  
RUN yaourt-install \  
ruby-iruby && \  
as-user iruby register --force && \  
yaourt-clean  
  
# Prepare image for running  
USER jupyter  
WORKDIR $NB_HOME  
COPY jupyter-run /usr/local/bin/jupyter-run  
  
EXPOSE 8888  
CMD jupyter-run  

