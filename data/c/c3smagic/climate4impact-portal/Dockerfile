FROM centos:7  
#TODO: put maintainer here  
#MAINTAINER Climate4Impact Team at KNMI <?@knmi.nl>  
VOLUME /config  
VOLUME /data  
  
EXPOSE 443  
RUN yum update -y && yum install -y \  
epel-release  
  
RUN yum clean all && yum groupinstall -y "Development tools"  
  
RUN yum update -y && yum install -y \  
hdf5-devel \  
netcdf \  
netcdf-devel \  
proj \  
proj-devel \  
sqlite \  
sqlite-devel \  
udunits2 \  
udunits2-devel \  
make \  
# conda dependency  
bzip2 \  
# adaguc dependencies  
libxml2-devel \  
cairo-devel \  
gd-devel \  
postgresql-devel \  
# java dependencies  
ant \  
tomcat \  
gdal-devel  
  
RUN mkdir /scr  
WORKDIR /src  
  
# conda  
RUN curl -L -O https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh  
RUN bash ./Miniconda2-latest-Linux-x86_64.sh -p /miniconda -b  
ENV PATH=/miniconda/bin:${PATH}  
RUN conda update -y conda  
RUN conda config --add channels conda-forge  
  
# isntall python dependencies  
RUN yes | pip install --upgrade pip  
RUN conda update -y conda && conda install -y \  
lxml \  
numpy \  
scipy \  
netcdf4 \  
python-dateutil \  
isodate \  
psycopg2 \  
requests \  
prov \  
pydotplus  
  
RUN pip install python-magic  
  
# PyWPS does not work with versions higher than 56 for icu due some missing
shared library issues  
#RUN conda install icu  
RUN conda install icu=56.1 -y  
  
# install icclim (will be conda in the future)  
RUN curl -L -O https://github.com/cerfacs-globc/icclim/archive/4.2.5.tar.gz  
RUN tar xvf 4.2.5.tar.gz  
WORKDIR /src/icclim-4.2.5  
RUN gcc -fPIC -g -c -Wall ./icclim/libC.c -o ./icclim/libC.o  
RUN gcc -shared -o ./icclim/libC.so ./icclim/libC.o  
RUN python setup.py install  
  
# install clipc combine toolkit  
RUN pip install
https://dev.knmi.nl/projects/clipccombine/repository/raw/dist/clipc_combine_process-1.6.tar.gz  
  
# install provenance toolkit  
WORKDIR /src  
RUN curl -L -O https://github.com/KNMI/wps_prov/archive/master.tar.gz  
RUN tar xvf master.tar.gz  
WORKDIR /src/wps_prov-master  
RUN python setup.py install  
  
# install pywps  
WORKDIR /src  
RUN curl -L -O https://github.com/geopython/pywps/archive/pywps-3.2.5.tar.gz  
RUN tar xvf pywps-3.2.5.tar.gz  
# the rest is setting up the env variables but those paths will depend on
monted data dir  
# install adaguc  
WORKDIR /src  
RUN curl -L https://github.com/KNMI/adaguc-server/archive/master.tar.gz >
adaguc-server.tar.gz  
RUN tar xvf adaguc-server.tar.gz  
RUN mv /src/adaguc-server-master /src/adaguc-server  
WORKDIR /src/adaguc-server  
ENV ADAGUCCOMPONENTS="-DENABLE_CURL -DADAGUC_USE_POSTGRESQL
-DADAGUC_USE_SQLITE -DADAGUC_USE_GDAL"  
RUN bash compile.sh  
# Copy adaguc binaries to /usr/bin  
RUN cp bin/* /usr/bin/  
  
# install impact portal  
WORKDIR /src  
COPY build.xml /src/climate4impact-portal/  
COPY src /src/climate4impact-portal/src/  
COPY WebContent /src/climate4impact-portal/WebContent/  
WORKDIR /src/climate4impact-portal  
ENV TOMCAT_LIBS=/usr/share/java/tomcat  
RUN ant  
  
# install impactportal wps scripts  
RUN mkdir /src/wpsprocesses  
WORKDIR /src/wpsprocesses  
RUN curl -L https://github.com/KNMI/impactwps/archive/master.tar.gz >
climate4impactwpsscripts.tar.gz  
RUN tar xvf climate4impactwpsscripts.tar.gz  
  
# Install certificates  
RUN mkdir -p /root/.globus/  
WORKDIR /root/.globus/  
RUN curl -L https://raw.githubusercontent.com/ESGF/esgf-
dist/master/installer/certs/esg_trusted_certificates.tar >
esg_trusted_certificates.tar  
RUN tar -xvf esg_trusted_certificates.tar  
RUN mv esg_trusted_certificates certificates  
  
# configure server  
RUN mv /usr/share/tomcat/conf/server.xml
/usr/share/tomcat/conf/server_oryg.xml  
RUN ln -s /config/server.xml /usr/share/tomcat/conf/server.xml  
RUN cp /src/climate4impact-portal/impactportal.war /usr/share/tomcat/webapps/  
ENV IMPACTPORTAL_CONFIG=/config/config.xml  
  
# TODO check why this is needed  
RUN conda install icu -y  
  
# Insert local instance trustroot into truststore  
#CMD keytool -export -alias tomcat -rfc -file
/root/.globus/certificates/tomcat.pem -keystore /config/c4i_keystore.jks
-storepass password  
#CMD keytool -import -v -trustcacerts -alias tomcat -file
/root/.globus/certificates/tomcat.pem -keystore /config/esg-truststore.ts
-storepass changeit -noprompt  
#CMD c_rehash /root/.globus/certificates  
#CMD /bin/bash  
CMD mkdir -p /data/wpsoutputs && \  
mkdir -p /data/c4i/climate4impact-portal/impactspace && \  
/usr/libexec/tomcat/server start  
  
#Build with docker build -t climate4impact-portal ./climate4impact-
portal/Docker/  
#This docker container needs to be runned with custom configuration settings:
docker run -i -t -p 443:443 -v $HOME/config:/config climate4impact-portal  
#Visit https://192.168.99.100/impactportal/ to go to the portal  

