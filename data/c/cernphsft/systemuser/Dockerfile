  
# Analogous to jupyter/systemuser, but based on CC7 and inheriting directly
from cernphsft/notebook.  
# Run with the DockerSpawner in JupyterHub.  
FROM cernphsft/notebook:v2.3  
MAINTAINER Enric Tejedor Saavedra <enric.tejedor.saavedra@cern.ch>  
  
RUN yum -y install yum-plugin-ovl # See https://github.com/CentOS/sig-cloud-
instance-images/issues/15  
  
# Disable requiretty and secure path - required by systemuser.sh  
RUN yum -y install sudo  
RUN sed -i'' '/Defaults \\+requiretty/d' /etc/sudoers  
RUN sed -i'' '/Defaults \\+secure_path/d' /etc/sudoers  
  
# Install ROOT prerequisites  
RUN yum -y install \  
libXpm \  
libXft  
  
# Install requests - required by jupyterhub-singleuser  
RUN pip3 install requests  
  
# Install bs4 - required by sparkconnector.serverextension  
RUN pip3 install bs4  
  
# Install tk - required by matplotlib  
RUN yum -y install tk  
  
# Install Cloudera dependencies - required by IT Spark clusters  
RUN yum -y install \  
alsa-lib \  
at \  
bc \  
cronie \  
cronie-anacron \  
crontabs \  
cvs \  
db4-cxx \  
db4-devel \  
ed \  
file \  
gdbm-devel \  
gettext \  
jpackage-utils \  
libXi \  
libXtst \  
man \  
passwd \  
pax \  
perl-CGI \  
perl-ExtUtils-MakeMaker \  
perl-ExtUtils-ParseXS \  
perl-Test-Harness \  
perl-Test-Simple \  
perl-devel \  
redhat-lsb-core \  
rsyslog \  
time \  
xz \  
xz-lzma-compat  
  
# Install openmotif - required by Geant4 (libXm)  
RUN yum -y install openmotif  
  
# Install libaio - required by Oracle  
RUN yum -y install libaio  
  
# Install cern-get-sso-cookie and update CERN CA certs - ATLAS TDAQ, UCA-63  
RUN yum -y install cern-get-sso-cookie  
RUN yum -y update CERN-CA-certs  
  
# Create truststore for NXCALS Spark connection  
RUN yum -y install java-1.8.0-openjdk && \  
keytool -import -alias cerngridCA -file
/etc/pki/tls/certs/CERN_Grid_Certification_Authority.crt -keystore
/etc/pki/tls/certs/truststore.jks -storepass 'password' -noprompt && \  
keytool -import -alias cernRootCA2 -file
/etc/pki/tls/certs/CERN_Root_Certification_Authority_2.crt -keystore
/etc/pki/tls/certs/truststore.jks -storepass 'password' -noprompt && \  
yum -y erase java-1.8.0-openjdk && \  
rm -rf /usr/lib/jvm/  
  
# Install HEP_OSlibs - includes atlas blas  
RUN yum -y install HEP_OSlibs_SL6  
  
# Clean the image  
RUN clean_requirements_on_remove=1 >> /etc/yum.conf && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
# WORKAROUND  
# Hide from Jupyter the Python3 kernel by hand  
RUN mv /usr/local/lib/python3.6/site-packages/ipykernel
/usr/local/lib/python3.6/site-packages/ipykernelBACKUP  
RUN mv /usr/local/share/jupyter/kernels /usr/local/share/jupyter/kernelsBACKUP  
  
#Add extra save to fileio  
ADD extra_save.d/fileio.py /usr/local/lib/python3.6/site-
packages/notebook/services/contents/fileio.py  
  
EXPOSE 8888  
ENV SHELL /bin/bash  
  
ADD systemuser.sh /srv/singleuser/systemuser.sh  
WORKDIR /root  
CMD ["sh", "/srv/singleuser/systemuser.sh"]  

