FROM tomcat:8.0-jre7  
MAINTAINER Milton Pividori <mpividori@sinc.unl.edu.ar>  
  
# Install needed packages  
RUN DEBIAN_FRONTEND=noninteractive \  
dpkg --add-architecture i386 && \  
apt-get update && apt-get install -y \  
wget \  
mercurial \  
libxt6 \  
libxmu6 \  
libxp6 \  
libxtst6 \  
libc6:i386 \  
libncurses5:i386 \  
libstdc++6:i386 && \  
apt-get clean && apt-get autoclean  
  
# Set up MATLAB binary  
RUN ln -s /MATLAB/bin/matlab /usr/local/bin/  
  
# Get war and clone repository  
RUN cd /usr/local/tomcat/webapps/ && wget https://bitbucket.org/sinc-
lab/webclusterensembles/downloads/web-cluster-ensembles.war  
RUN hg clone -b stable https://bitbucket.org/sinc-lab/webclusterensembles
/repo  
  
# Set up MATLAB code and METIS  
RUN ln -s /repo/src/MatlabScript /usr/local/tomcat  
ENV PMETIS_PATH '/usr/local/tomcat/MatlabScript/ClusterEnsemble-V2.0/pmetis'  
ENV SHMETIS_PATH '/usr/local/tomcat/MatlabScript/ClusterEnsemble-V2.0/shmetis'  
ENV WCE_HBM2DDL_AUTO 'create'  

