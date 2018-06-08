FROM simsofast/base  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
WORKDIR /tmp  
  
# Install SU2 (with its own py2 enviroment)  
ARG RUN_REGRESSION  
ENV SU2_RUN /usr/local/bin  
ENV SU2_HOME /opt/su2  
ENV PATH $PATH:$SU2_RUN  
ENV PYTHONPATH $PYTHONPATH:$SU2_RUN  
COPY install_su2.sh /tmp  
RUN bash install_su2.sh \  
&& rm install_su2.sh  
  
WORKDIR /root  

