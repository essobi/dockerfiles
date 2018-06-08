FROM centos:7  
MAINTAINER Matt Eldridge "matthew.eldridge@cruk.cam.ac.uk"  
RUN yum groupinstall -y 'development tools'  
RUN yum install -y wget libxml2-devel libcurl-devel openssl-devel  
  
RUN wget https://download3.rstudio.org/centos6.3/x86_64/shiny-
server-1.5.5.872-rh6-x86_64.rpm  
RUN yum install -y --nogpgcheck shiny-server-1.5.5.872-rh6-x86_64.rpm  
RUN rm shiny-server-1.5.5.872-rh6-x86_64.rpm  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum install -y R  
  
RUN R -e 'install.packages(c("shiny", "rmarkdown"), repos =
"https://cloud.r-project.org")'  
RUN R -e 'install.packages("tidyverse", repos =
"https://cloud.r-project.org")'  
  
EXPOSE 3838  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
RUN chmod ugo+rx /usr/bin/shiny-server.sh  
  
# ensure the user account that is running the shiny server process has write
privilege for /var/lib/shiny-server  
RUN chmod ugo+rwx /var/lib/shiny-server  
  
CMD ["/usr/bin/shiny-server.sh"]  
  

