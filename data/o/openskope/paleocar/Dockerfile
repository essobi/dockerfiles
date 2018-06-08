from openskope/feddata:0.1.2  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
  
RUN echo '***** install the bocinsky/paleocar package from GitHub *****' \  
&& echo 'devtools::install_github("bocinsky/paleocar")' >
/tmp/install_paleocar.R \  
&& R --no-save < /tmp/install_paleocar.R  
  
USER skope  
  
CMD echo "Usage: docker run openskope/paleocar Rscript <r-script-using-
paleocar> [r-script-arguments]"

