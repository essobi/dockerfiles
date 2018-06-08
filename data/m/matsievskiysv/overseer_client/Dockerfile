FROM matsievskiysv/shiny-server  
MAINTAINER Matsievskiy Sergey "MatsievskiySV@gmail.com"  
USER root  
RUN apt-get update && apt-get install -y git default-libmysqlclient-dev  
RUN R -e "install.packages(c('rhandsontable', 'RMySQL'),
repos='https://cran.rstudio.com/')"  
RUN git clone https://seregaxvm@bitbucket.org/seregaxvm/overseer_client.git
/srv/shiny-server/overseer-ui  
  
USER shiny  
CMD ["/usr/bin/shiny-server"]  

