FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update  
RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list'  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
RUN gpg -a --export E084DAB9 | sudo apt-key add -  
RUN apt-get update  
RUN apt-get -y install r-base  
RUN R -e "install.packages('shiny', repos='https://cran.rstudio.com/')"  
RUN apt-get install -y gdebi-core wget  
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.5.1.834-amd64.deb  
RUN gdebi -n shiny-server-1.5.1.834-amd64.deb  
RUN mkdir /srv/shiny-server/fgsea && cd /srv/shiny-server/fgsea && wget
https://github.com/pinguinson/fgsea-web/archive/v0.1.3.tar.gz -O - | tar xz
--strip=1  
RUN mkdir /srv/shiny-server/fgsea/www/img && chown shiny /srv/shiny-
server/fgsea/www/img  
# installing dependencies  
RUN apt-get install -y libcairo2-dev  
RUN R -e "install.packages(c('rmarkdown', 'shinyjs', 'DT', 'shinydashboard',
'svglite', 'hash'), repos='https://cran.rstudio.com/')"  
RUN R -e 'source("https://bioconductor.org/biocLite.R"); biocLite(c("fgsea",
"org.Hs.eg.db", "org.Mm.eg.db", "AnnotationDbi"))'  
EXPOSE 3838  
CMD shiny-server --pidfile=/var/run/shiny-server.pid >> /var/log/shiny-
server.log 2>&1  

