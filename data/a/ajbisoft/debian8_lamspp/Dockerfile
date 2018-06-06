FROM ajbisoft/debian8_lapp  
MAINTAINER Jakub Kwiatkowski <jakub@ajbisoft.pl>  
RUN apt-get update && apt-get install -y php5-mssql \  
&& apt-get -y --purge autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/*  

