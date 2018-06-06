FROM ajbisoft/debian8_lap  
MAINTAINER Jakub Kwiatkowski <jakub@ajbisoft.pl>  
RUN apt-get update && apt-get install -y php5-mysql mysql-client \  
&& apt-get -y --purge autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/*  

