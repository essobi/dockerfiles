FROM jupyter/datascience-notebook  
  
# Install additional libraries  
RUN conda install -c conda-forge elasticsearch  
RUN conda install --quiet --yes 'tensorflow=1.0*' pyodbc  
#RUN conda install --quiet --yes -n python2 'tensorflow=1.0*'  
RUN conda install -y -c conda-forge alpenglow pyarrow matplotlib  
RUN conda install -y -c anaconda seaborn pyspark  
  
# Switch to root mode to install packages  
USER root  
  
# Install zeppelin  
# RUN curl http://apache.panu.it/zeppelin/zeppelin-0.7.2/zeppelin-0.7.2-bin-
all.tgz -o zeppelin.tgz  
# RUN tar -xvf zeppelin.tgz && \  
# rm zeppelin.tgz  
# Installing Java, Pegdown and MS SQL drivers  
RUN apt-get update  
RUN apt-get install apt-transport-https apt-utils -y  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
  
# Adding MS SQL deps  
RUN \  
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \  
curl https://packages.microsoft.com/config/debian/8/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
# Install Java and MS SQL Drivers  
RUN \  
apt-get update && \  
ACCEPT_EULA=Y apt-get install msodbcsql unixodbc-dev oracle-java8-installer
libpegdown-java openconnect -y  
  
#Switch back to user mode  
#USER $NB_USER  
VOLUME /home/$NB_USER/work  
WORKDIR /home/$NB_USER/work  
  
# The interpretor uses the system python, we need the conda one  
ENV PYTHONPATH=/opt/conda/bin/python  
COPY ./run.sh /home/$NB_USER/run.sh  
# Remomve this line to disable VPN  
CMD ["/home/jovyan/run.sh"]  
  
# Remove this line to start a Jupyter Notebook  
# CMD ["/home/$NB_USER/zeppelin/bin/zeppelin.sh"]  

