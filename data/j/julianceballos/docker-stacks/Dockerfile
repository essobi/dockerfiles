# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/pyspark-notebook  
  
MAINTAINER Jupyter Project <jupyter@googlegroups.com>  
  
USER root  
  
# RSpark config  
ENV R_LIBS_USER $SPARK_HOME/R/lib  
  
# R pre-requisites  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
fonts-dejavu \  
gfortran \  
gcc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Postgresql pre-requisites  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -  
RUN apt-get update && \  
apt-get install -y \  
postgresql-9.4 \  
libpq-dev  
  
USER postgres  
  
# Start and initialize postgresql  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\  
createdb -O docker docker  
  
# Allow connections  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.4/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf  
  
USER $NB_USER  
  
# R packages  
# Pin r-base to a specific build number for https://github.com/jupyter/docker-
stacks/issues/210#issuecomment-246081809  
RUN conda config --add channels r && \  
conda install --quiet --yes \  
'r-base=3.3.1 1' \  
'r-irkernel=0.7*' \  
'r-ggplot2=2.1*' \  
'r-rcurl=1.95*' && conda clean -tipsy  
  
# Apache Toree kernel  
RUN pip install --upgrade pip  
RUN pip --no-cache-dir install
https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0/snapshots/dev1/toree-
pip/toree-0.2.0.dev1.tar.gz  
RUN pip install psycopg2  
RUN jupyter toree install --user  

