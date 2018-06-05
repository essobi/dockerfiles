FROM pradosj/docker-ngs  
  
  
# install R  
RUN apt-get update && apt-get install -y apt-transport-https software-
properties-common  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
E298A3A825C0D65DFD57CBB651716619E084DAB9  
RUN add-apt-repository 'deb [arch=amd64,i386]
https://cran.rstudio.com/bin/linux/ubuntu xenial/'  
RUN apt-get update && apt-get install -y r-base libcurl4-openssl-dev libssl-
dev libmariadb-client-lgpl-dev libxml2-dev pandoc  
  
# install R packages  
RUN Rscript -e
'install.packages(c("ggplot2","devtools","igraph","visNetwork"),repos="https://stat.ethz.ch/CRAN/")'  
RUN Rscript -e
'source("https://bioconductor.org/biocLite.R");biocLite(c("rtracklayer","Rsamtools","GenomicAlignments","GenomicFeatures"))'  
  
# Try to generate an HTML retport  
#RUN apt-get update && apt-get install -y python3-pip  
#RUN cd /tmp && git clone https://github.com/igvteam/igv.js-reports.git && cd
igv.js-reports/ && pip3 install -r requirements.txt  
# Try report with flask  
#git clone https://github.com/igvteam/igv.js-flask.git  
ADD Makefile /tmp/Makefile  
ADD Analyse_bam.R /tmp/Analyse_bam.R  
ADD SA564.fa SA564.gff /tmp/  
ENV MAKEFILES /tmp/Makefile  
  
WORKDIR /export  
  
VOLUME ["/export/"]  
ENTRYPOINT ["make"]  
#EXPOSE :80  

