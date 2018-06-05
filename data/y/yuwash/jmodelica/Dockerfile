FROM ubuntu:16.04  
MAINTAINER alimguzhin@di.uniroma1.it  
  
COPY *.sh /build/  
  
ENV JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"  
RUN set -ex \  
&& /build/prepare.sh \  
&& /build/jmodelica.sh \  
&& /build/cleanup.sh \  
&& rm -rf /build  
  
ENV JMODELICA_HOME="/opt/jmodelica"  
ENV IPOPT_HOME="/opt/ipopt"  
ENV CPPAD_HOME="/opt/jmodelica/ThirdParty/CppAD"  
ENV SUNDIALS_HOME="/opt/jmodelica/ThirdParty/Sundials"  
ENV PYTHONPATH="/opt/jmodelica/Python"  
ENV
LD_LIBRARY_PATH="/opt/ipopt/lib:/opt/jmodelica/ThirdParty/Sundials/lib:/opt/jmodelica/ThirdParty/CasADi/lib"  
ENV SEPARATE_PROCESS_JVM="/usr/lib/jvm/java-8-openjdk-amd64"  
ENV MODELICAPATH="/opt/jmodelica/ThirdParty/MSL:/home/docker/modelica"  
ENV USER docker  
WORKDIR /home/docker  
  
CMD ["/opt/jmodelica/bin/jm_ipython.sh"]  

