FROM cern/cc7-base  
  
# RUN yum -y update  
RUN yum -y install git xrootd-client python-pip globus-proxy-utils  
RUN pip install --upgrade pip  
RUN pip install git+https://github.com/sashabaranov/easywebdav.git  
RUN pip install git+https://github.com/skygrid/hep-data-backends.git  
RUN pip install click  
  
ENV X509_CERT_DIR /etc/pki/tls/certs  
  
  
# Reduce container size  
RUN localedef --list-archive | grep -v -i ^en | xargs localedef --delete-from-
archive  
RUN mv /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl  
RUN build-locale-archive  
  
RUN yum -y autoremove  
RUN find /usr/share/locale | grep -v en | xargs rm -rf  
RUN yum clean all

