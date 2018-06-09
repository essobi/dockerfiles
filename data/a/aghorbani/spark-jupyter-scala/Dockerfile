FROM aghorbani/spark-miniconda:2.1.0-3.4  
MAINTAINER Asghar Ghorbani [https://de.linkedin.com/in/aghorbani]  
  
# Install Scala kernel for Jupyter  
RUN curl -L -o /usr/local/bin/coursier
https://raw.githubusercontent.com/alexarchambault/coursier/e70c32f/coursier &&
\  
chmod +x /usr/local/bin/coursier && \  
curl -L -o jupyter-scala
https://raw.githubusercontent.com/alexarchambault/jupyter-
scala/18b507d/jupyter-scala && \  
chmod +x jupyter-scala && \  
./jupyter-scala  
  
# Install Java 8u112  
RUN curl -LO "http://download.oracle.com/otn-
pub/java/jdk/8u112-b15/jdk-8u112-linux-x64.rpm" -H 'Cookie:
oraclelicense=accept-securebackup-cookie' && \  
rpm -i jdk-8u112-linux-x64.rpm && \  
rm jdk-8u112-linux-x64.rpm  
  
# Install Toree  
COPY toree-0.2.0.dev1.tar.gz .  
RUN pip install toree-0.2.0.dev1.tar.gz && \  
rm toree-0.2.0.dev1.tar.gz && \  
jupyter toree install --ToreeInstall.prefix=$CONDA_DIR
\--interpreters=PySpark,SQL,Scala,SparkR  
  
# Install nodejs, npm and bower. They are needed for
jupyter_declarativewidgets  
RUN yum install -y epel-release && \  
rm /var/lib/rpm/__db* && \  
rpm --rebuilddb && \  
yum install -y nodejs && \  
yum install -y npm && \  
yum clean all && \  
npm install -g bower  
  
# Install Visulization tools for Jupyter  
RUN conda install vega --channel conda-forge -y && \  
conda install plotly -y && \  
pip install jupyter_declarativewidgets && \  
jupyter declarativewidgets quick-setup --sys-prefix && \  
pip install jupyter_dashboards && \  
jupyter dashboards quick-setup --sys-prefix && \  
conda clean -tipsy  
  
RUN conda install -c r r-essentials=1.5.0  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
ADD jupyter_notebook.sh /etc/jupyter_notebook.sh  
CMD ["/etc/jupyter_notebook.sh"]  
  

