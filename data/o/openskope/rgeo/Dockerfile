from openskope/gdal:0.1.1  
ARG DEBIAN_FRONTEND=noninteractive  
USER root  
  
ENV DOCKER_IMAGE_NAME openskope/rgeo  
  
RUN echo "***** install R directly from CRAN apt server *****" \  
&& echo deb http://cran.rstudio.com/bin/linux/ubuntu xenial/ >
/etc/apt/sources.list.d/cran.list \  
&& gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add - \  
&& apt-get -y update \  
&& apt-get -y install r-base \  
\  
&& echo "***** install libproj cartographic projection library *****" \  
&& apt-get -y install libproj-dev \  
\  
&& echo "***** install GEOS libraries *****" \  
&& apt-get -y install libgeos-3.5.0 libgeos-dev \  
\  
&& echo "***** install netcdf and netcdf development libraries *****" \  
&& apt-get -y install netcdf-bin libnetcdf-dev  
  
RUN echo '***** install curl and ssl development libraries needed by devtools
***** ' \  
&& apt-get -y install libcurl4-openssl-dev libssl-dev \  
\  
&& echo "***** install libxml development package *****" \  
&& apt-get -y install libxml2-dev  
  
RUN echo '***** install R scripting support packages *****' \  
&& echo 'install.packages(c("optparse", "magrittr", "tidyverse", "XML"),
repos="http://cran.us.r-project.org")' \  
> /tmp/install_r_scripting_packages.R \  
&& R --no-save < /tmp/install_r_scripting_packages.R \  
\  
&& echo '***** install R packages for geospatial computing *****' \  
&& echo 'install.packages(c("rgdal", "rgeos", "raster", "ncdf4"),
repos="http://cran.us.r-project.org")' \  
> /tmp/install_geospatial_r_packages.R \  
&& R --no-save < /tmp/install_geospatial_r_packages.R  
  
USER skope  
  
ENV SELFTEST_DIR ${SELFTEST_BASE}/${DOCKER_IMAGE_NAME}  
COPY ./selftest/expected.txt ${SELFTEST_BASE}  
COPY ./selftest/test.sh ${SELFTEST_DIR}/  
RUN ${SELFTEST_BASE}/runtest.sh  
  
CMD echo "Usage: docker run openskope/rgeo Rscript <r-script-file> [r-script-
arguments]"

