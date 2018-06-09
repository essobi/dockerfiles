FROM agaveapi/htcondor  
MAINTAINER Andres Herrera "fabio.herrera@correounivalle.edu.co"  
RUN yum clean all  
RUN yum install yum-skip-broken -y  
RUN yum install subversion -y  
RUN yum install gcc-c++ -y  
RUN yum install sqlite-devel -y  
RUN yum install libxml2-devel -y  
RUN yum install python-devel -y  
RUN yum install numpy -y  
RUN yum install swig -y  
RUN yum install expat-devel -y  
RUN yum install libcurl-devel -y  
RUN yum install geos -y  
RUN yum install geos-devel -y  
RUN yum install gdal -y  
RUN yum install gdal-devel -y  
RUN yum install proj -y  
RUN yum install proj-nad -y  
RUN yum install proj-epsg -y  
RUN yum install proj-devel -y  
RUN yum install udunits2-devel -y  
RUN yum install R -y  
RUN R -e "install.packages(c('raster')
,repos='https://cloud.r-project.org/',dependencies=TRUE)"  
RUN R -e "install.packages(c('rgeos')
,repos='https://cloud.r-project.org/',dependencies=TRUE)"  
RUN R -e "install.packages(c('rgdal')
,repos='https://cloud.r-project.org/',dependencies=TRUE)"  
RUN echo "END Dependencies"  

