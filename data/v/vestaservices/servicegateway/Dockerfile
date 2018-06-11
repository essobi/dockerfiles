FROM centos:7  
# Ensure appropriates locales are generated  
RUN sed -ie
's/^override_install_langs.*/override_install_langs=fr_CA.utf8,en_CA.utf8/'
/etc/yum.conf  
  
# Install required libraries -------------------------------  
RUN yum install -y \  
python2-devel \  
gcc \  
wget \  
tar  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
python ./get-pip.py  
  
# Install external dependencies -------------------  
RUN pip install python-swiftclient \  
python-keystoneclient \  
gunicorn \  
nose  
  
# Set environment encoding for STDOUT ------------  
RUN yum -y -q reinstall glibc-common # We need to do this to reactivate the
locale defs.  
ENV LC_ALL en_CA.utf8  
  
# Application -------------------------------------  
COPY . /var/local/src/ServiceGateway  
  
RUN pip install /var/local/src/ServiceGateway  
  
EXPOSE 5000  
RUN nosetests -v ServiceGateway  
  
ENTRYPOINT ["gunicorn", "ServiceGateway.rest_api:APP"]  
  
CMD ["-w", "4", "-preload", "-b", "0.0.0.0:5000", "--log-
config=/var/local/src/ServiceGateway/ServiceGateway/logging.ini"]  

