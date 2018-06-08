############################################################  
# Dockerfile to build LPPic  
# Based on Fedora base image  
############################################################  
  
# Set the base image from jeandet  
FROM jeandet/teamcity-docker-minimal-agent  
LABEL maintainer "Antoine Tavant <antoine.tavant@lpp.polytechnique.fr>"  
  
# Update the repository sources list  
#RUN dnf -y update  
  
################## BEGIN INSTALLATION ######################  
  
RUN dnf install -y git openmpi-devel cmake hdf5-openmpi-devel petsc-openmpi-
devel hypre* gcc-gfortran module-macros gcc-c++ zlib-devel wget  
  
  
RUN echo "system.lppic=true" >>
/opt/buildagent/conf/buildAgent.dist.properties  
  
  
#--------------------------------------------------------------  
#LD_LIBRARY_PATH  
#--------------------------------------------------------------  
RUN export LD_LIBRARY_PATH=/usr/lib64/openmpi/lib/  
ENV PATH=${PATH}:/usr/lib64  
#HDF5_INCLUDE=/usr/lib64/openmpi/include  
#HDF5_LIB=/usr/lib64/gfortran/modules/openmpi/  
#PETSC_DIR  
#HYPRE_DIR  
  
RUN export HDF5_DIR=/usr/lib64/openmpi/  
CMD ["module load mpi/openmpi-x86_64"]  
CMD ["/run-services.sh"]  

