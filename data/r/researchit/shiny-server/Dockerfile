FROM centos/s2i-core-centos7  
  
LABEL maintainer="Levi Baber <baber@iastate.edu>"  
  
#package installation  
RUN yum -y install epel-release && \  
yum -y install R && \  
Rscript -e "install.packages('shiny', repos='https://cran.rstudio.com/')" && \  
yum -y install wget && \  
wget https://download3.rstudio.org/centos5.9/x86_64/shiny-
server-1.5.6.875-rh5-x86_64.rpm && \  
yum -y install --nogpgcheck shiny-server-1.5.6.875-rh5-x86_64.rpm && \  
yum -y install git && \  
sed -i -e 's|/srv/shiny-server|/opt/app-root|g' /etc/shiny-server/shiny-
server.conf && \  
sed -i -e 's/run_as shiny;/run_as 1001;/g' /etc/shiny-server/shiny-
server.conf;  
  
USER 1001  
EXPOSE 3838  
STOPSIGNAL SIGTERM  
  
CMD ["/opt/shiny-server/bin/shiny-server", "-g", "daemon off;"]  
  

