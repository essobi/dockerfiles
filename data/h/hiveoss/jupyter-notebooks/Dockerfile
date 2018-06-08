FROM jupyter/minimal-notebook  
MAINTAINER eterna2 <eterna2@hotmail.com>  
  
USER root  
  
# Spark dependencies  
ENV APACHE_SPARK_VERSION 1.5.2  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends openjdk-7-jre-headless && \  
apt-get clean  
RUN wget -qO -
http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-
hadoop2.6.tgz | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6 spark  
# Spark pointers  
ENV SPARK_HOME /usr/local/spark  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip  
  
  
  
# Scala Spark kernel (build and cleanup)  
RUN cd /tmp && \  
echo deb http://dl.bintray.com/sbt/debian / > /etc/apt/sources.list.d/sbt.list
&& \  
apt-get update && \  
git clone https://github.com/ibm-et/spark-kernel.git && \  
apt-get install -yq --force-yes --no-install-recommends sbt && \  
cd spark-kernel && \  
git checkout 29856a785a && \  
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
  
# Scala Spark kernel spec  
RUN mkdir -p /opt/conda/share/jupyter/kernels/scala  
COPY kernels/scala.json /opt/conda/share/jupyter/kernels/scala/kernel.json  
  
# Node  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.1.1  
RUN apt-get -y update && \  
apt-get install -y curl libzmq3-dev && \  
apt-get clean  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
# iJavascript  
RUN npm install -g ijavascript mrcluster npmi  
  
# install iJavascript kernel  
RUN mkdir -p /opt/conda/share/jupyter/kernels/javascript  
COPY kernels/nodejs.json
/opt/conda/share/jupyter/kernels/javascript/kernel.json  
  
# Python dependencies  
RUN apt-get -y update && \  
apt-get install -y python-qt4 && \  
apt-get clean  
  
# Python 2  
USER jovyan  
  
# Install Python 2 packages  
RUN conda install --yes \  
'python=2.7*' \  
'ipython=4.0*' \  
'ipywidgets=4.0*' \  
'pandas=0.16*' \  
'matplotlib=1.4*' \  
'scipy=0.15*' \  
'seaborn=0.6*' \  
'scikit-learn=0.16*' \  
'scikit-image=0.11*' \  
'sympy=0.7*' \  
'cython=0.22*' \  
'patsy=0.3*' \  
'statsmodels=0.6*' \  
'cloudpickle=0.1*' \  
'dill=0.2*' \  
'numba=0.20*' \  
'bokeh=0.9*' \  
'gensim=0.12*' \  
pyzmq \  
&& conda clean -yt  
  
USER root

