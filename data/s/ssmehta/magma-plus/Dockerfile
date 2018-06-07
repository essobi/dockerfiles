FROM ssmehta/magma:latest  
MAINTAINER Sajjan Singh Mehta "sajjan.s.mehta@gmail.com"  
# Set home directory  
ENV HOME /root  
WORKDIR /root  
  
# Set MAGMA+ version  
ENV MAGMAPLUS_VERSION 1.0.1  
# Get MAGMa+  
ADD https://github.com/savantas/MAGMa-plus/archive/v$MAGMAPLUS_VERSION.tar.gz
/root/  
RUN tar xzvf v$MAGMAPLUS_VERSION.tar.gz && \  
rm v$MAGMAPLUS_VERSION.tar.gz && \  
mv MAGMa-plus-$MAGMAPLUS_VERSION MAGMa-plus  
  
# Configrue MAGMa+  
RUN cd /root/MAGMa-plus && \  
unzip metabolite_posD_rfc.pkl.zip && \  
unzip metabolite_negC_rfc.pkl.zip  
  
ENV MAGMAPLUS_CLASSIFIER_PATH /root/MAGMa-plus  

