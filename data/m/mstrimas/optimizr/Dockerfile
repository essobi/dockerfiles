FROM rocker/hadleyverse:latest  
MAINTAINER Matt Strimas-Mackey <mstrimas@gmail.com>  
  
# Install linear programming solvers  
# GEOS and GDAL GIS libraries are required for some R packages  
RUN apt-get update \  
&& apt-get install -y apt-utils libgdal-dev libproj-dev libgeos-dev \  
&& apt-get install -y coinor-libsymphony-dev coinor-libcgl-dev libglpk-dev  
  
# Install R packages for LP solvers  
RUN install2.r --error \  
lpSolve \  
lpSolveAPI \  
Rsymphony \  
clpAPI \  
Rglpk \  
glpkAPI \  
&& installGithub.r Bioconductor-mirror/lpsymphony  
  
# Copy Gurobi files and install Gurobi and R package  
# Can't directly install because no direct link to install files  
COPY gurobi6.5.1_linux64.tar.gz /  
RUN tar -xzf /gurobi6.5.1_linux64.tar.gz -C /opt/ \  
&& install2.r --error \  
/opt/gurobi651/linux64/R/gurobi_6.5-1_R_x86_64-unknown-linux-gnu.tar.gz \  
&& ln -s /opt/gurobi651/linux64/lib/libgurobi65.so /lib/libgurobi65.so  
ENV PATH $PATH:/opt/gurobi651/linux64/bin"  

