FROM ubuntu:artful  
  
MAINTAINER Francesco Serafin <francesco.serafin.3@gmail.com>, Olaf David
<odavid@colostate.edu>  
  
ENV OMS_VERSION="3.5.52"  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/ \  
simulation=/work/simulation/Simulation.sim \  
LD_LIBRARY_PATH=/usr/local/lib/python2.7/dist-packages/jep \  
R_LIBS=/work/Rlibs/build/ \  
PYTHONPATH=$PYTHONPATH:/work/Pylibs/ \  
OMS_CONSOLE="oms-$OMS_VERSION-console"  
# copy OMS console, entrypoint.sh, packageParser.py and package.json into the
container  
COPY $OMS_CONSOLE.zip entrypoint.sh ./  
COPY rdep.R /usr/bin/  
COPY bash_script/ ./bash_script/  
  
RUN set -x \  
\  
&& apt-get -y update \  
\  
# installation of required packages  
&& apt-get install --no-install-recommends -y \  
ca-certificates \  
wget \  
binutils \  
gcc \  
g++ \  
gfortran \  
make \  
unzip \  
python-dev \  
openjdk-8-jdk \  
ant \  
python-pip \  
r-base \  
libblas-dev \  
liblapack-dev \  
libgdal-dev \  
libproj-dev \  
lynx \  
libssl-dev \  
libcurl4-gnutls-dev \  
\  
# install setuptools wheel and jep python packages  
&& pip2 install setuptools \  
&& pip2 install wheel \  
&& pip2 install jep==3.6.4 \  
\  
# get latest version of Rserve and Rcpp, then install them  
&& CRAN="https://cran.r-project.org/src/contrib/" \  
&& PKGCONFIG=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/pkgconfig_/p' ) \  
&& echo $PKGCONFIG | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL pkgconfig_*.tar.gz \  
&& rm pkgconfig_*.tar.gz \  
&& MATRIX=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/Matrix_/p' ) \  
&& echo $MATRIX | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL Matrix_*.tar.gz \  
&& rm Matrix_*.tar.gz \  
&& MAGRITTR=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/magrittr_/p' ) \  
&& echo $MAGRITTR | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL magrittr_*.tar.gz \  
&& rm magrittr_*.tar.gz \  
&& IRLBA=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/irlba_/p' ) \  
&& echo $IRLBA | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL irlba_*.tar.gz \  
&& rm irlba_*.tar.gz \  
&& R6=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n '/\/R6_/p'
) \  
&& echo $R6 | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL R6_*.tar.gz \  
&& rm R6_*.tar.gz \  
&& OPENSSL=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/openssl_/p' ) \  
&& echo $OPENSSL | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL openssl_*.tar.gz \  
&& rm openssl_*.tar.gz \  
&& CURL=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/curl_/p' ) \  
&& echo $CURL | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL curl_*.tar.gz \  
&& rm curl_*.tar.gz \  
&& MIME=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/mime_/p' ) \  
&& echo $MIME | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL mime_*.tar.gz \  
&& rm mime_*.tar.gz \  
&& JSONLITE=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/jsonlite_/p' ) \  
&& echo $JSONLITE | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL jsonlite_*.tar.gz \  
&& rm jsonlite_*.tar.gz \  
&& IGRAPH=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/igraph_/p' ) \  
&& echo $IGRAPH | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL igraph_*.tar.gz \  
&& rm igraph_*.tar.gz \  
&& XML=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/XML_/p' ) \  
&& echo $XML | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL XML_*.tar.gz \  
&& rm XML_*.tar.gz \  
&& HTTR=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/httr_/p' ) \  
&& echo $HTTR | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL httr_*.tar.gz \  
&& rm httr_*.tar.gz \  
&& MINICRAN=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/miniCRAN_/p' ) \  
&& echo $MINICRAN | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL miniCRAN_*.tar.gz \  
&& rm miniCRAN_*.tar.gz \  
&& RSERVE=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/Rserve_/p' ) \  
&& echo $RSERVE | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL Rserve_*.tar.gz \  
&& rm Rserve_*.tar.gz \  
&& RCPP=$( lynx -dump -listonly "${CRAN}" | awk '{print $2}' | sed -n
'/\/Rcpp_/p' ) \  
&& echo $RCPP | awk '{print $1}' | xargs wget \  
&& R CMD INSTALL Rcpp_*.tar.gz \  
&& rm Rcpp_*.tar.gz \  
\  
# oms set up  
&& unzip $OMS_CONSOLE.zip \  
&& rm $OMS_CONSOLE.zip \  
&& mkdir -p /root/.oms/$OMS_VERSION/ \  
&& cp $OMS_CONSOLE/lib/cpptasks-1.0b6-od.jar /root/.oms/$OMS_VERSION/ \  
&& cp $OMS_CONSOLE/lib/groovy-all-2.3.9.jar /root/.oms/$OMS_VERSION/ \  
&& cp $OMS_CONSOLE/lib/jcommon-1.0.15.jar /root/.oms/$OMS_VERSION/ \  
&& cp $OMS_CONSOLE/lib/jfreechart-1.0.12.jar /root/.oms/$OMS_VERSION/ \  
&& cp $OMS_CONSOLE/lib/oms-all.jar /root/.oms/$OMS_VERSION/ \  
\  
&& mkdir /work \  
&& chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

