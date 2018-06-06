FROM jupyter/r-notebook  
MAINTAINER Will Price <will.price94@gmail.com>  
  
USER root  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
default-jdk \  
wget  
  
USER $NB_USER  
  
# R Packages  
RUN conda install --quiet --yes \  
'r-rjava'  
  
# By default R fails to find jni.h so we specify the include directory  
# manually  
RUN R CMD javareconf JAVA_CPPFLAGS=-I/usr/lib/jvm/default-java/include  
  
# Installing RWeka fails unless we set the LD_LIBRARY_PATH to point to  
# paths containing libjvm.so  
ENV LD_LIBRARY_PATH=/usr/lib/jvm/default-
java/jre/lib/amd64/server:/usr/lib/jvm/default-java/jre/lib/amd64  
  
COPY Rprofile.site /opt/conda/lib/R/etc/Rprofile.site  
  
COPY party.R /tmp  
RUN R -f /tmp/party.R  
  
COPY weka.R /tmp  
RUN R -f /tmp/weka.R  
  
# Python packages  
RUN conda install --quiet --yes \  
'scikit-learn' \  
'pandas' \  
'numpy' \  
'matplotlib'  

