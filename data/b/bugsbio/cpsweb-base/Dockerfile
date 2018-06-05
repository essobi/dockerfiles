FROM dockerfile/java  
  
RUN add-apt-repository "deb http://cran.rstudio.com/bin/linux/ubuntu
$(lsb_release -cs)/"  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN apt-get update -y  
  
RUN apt-get install -y libpq-dev r-recommended littler  
RUN /usr/share/doc/littler/examples/install.r gtools fMultivar RPostgreSQL
Rserve  
RUN cd /data && wget http://www.commanster.eu/rcode/rmutil.tgz && r -e
'install.packages("rmutil.tgz", repo=NULL)'  

