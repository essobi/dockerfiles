FROM fasrc/rshiny_pro_centos:latest  
  
RUN yum install -y postgresql-devel wget  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \  
chmod +x /usr/local/bin/dumb-init  
  
RUN R -e "install.packages(c('plotly', 'DT', 'RPostgreSQL',
'data.table','dplyr','car','scales','devtools'),
repos='https://cran.rstudio.com/', INSTALL_opts=c('--no-html', '--no-docs', '
--without-keep.source', '--clean'))"  
  
# these are two packages we need to show a loading screen while data are
loaded from db  
RUN R -e "install.packages(c('shinyjs', 'shinycssloaders'),
repos='https://cran.rstudio.com/', INSTALL_opts=c('--no-html', '--no-docs', '
--without-keep.source', '--clean'))"  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
#install rstudio  
RUN wget https://download2.rstudio.org/rstudio-server-rhel-
pro-1.0.153-x86_64.rpm && yum install -y --nogpgcheck rstudio-server-rhel-
pro-1.0.153-x86_64.rpm && yum clean all && rm -f /var/lib/rpm/__db* && rm -rfv
/var/cache/yum/*.*  
COPY rstudio-server.sh /usr/bin/rstudio-server.sh  
  
#setup supervisord to be able to run both services  
RUN yum -y install python-setuptools && easy_install supervisor  
  
RUN chmod +x /usr/bin/*sh  
  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 80 8080 8443 443 3838 8787  
ENTRYPOINT ["/usr/bin/supervisord" , "-c" ,"/etc/supervisor/supervisord.conf"]  
  

