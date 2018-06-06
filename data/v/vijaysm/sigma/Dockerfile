# Builds a Docker image with the official SIGMA packages  
# installed.  
#  
# Currently only MOAB is pre-installed in the image.  
#  
# Authors:  
# Vijay Mahadevan <vijay.m@gmail.com>  
FROM vijaysm/scientific:latest  
MAINTAINER Vijay Mahadevan <vijay.m@gmail.com>  
  
#  
# Select the latest stable releases of MOAB and VisIt.  
#  
ENV CGM_VERSION 16.0  
ENV MOAB_VERSION 4.9.3  
ENV VISIT_VERSION 2_12_1  
ENV ENABLE_DEBUG yes  
  
ENV HOME /home/sigma  
ENV CGM_DIR /opt/cgm-$CGM_VERSION  
ENV MOAB_DIR /opt/moab-$MOAB_VERSION  
ENV VISIT_DIR /opt/visit  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install Visit for visualization  
#RUN wget --no-verbose -O visit-$VISIT_VERSION.tar.gz visit
http://portal.nersc.gov/project/visit/releases/2.12.1/visit$VISIT_VERSION.linux-x86_64-ubuntu14.tar.gz
&& \  
# tar -xzf visit-$VISIT_VERSION.tar.gz && \  
# mv visit$VISIT_VERSION.linux-x86_64 /opt/visit && rm -f
visit-$VISIT_VERSION.tar.gz && \  
# echo "export PATH=$PATH:$VISIT_DIR/bin" >> $HOME/.bashrc  
# Install MOAB from latest stable  
ADD scripts/install*.sh /tmp/  
RUN bash /tmp/install_all.sh  
  

