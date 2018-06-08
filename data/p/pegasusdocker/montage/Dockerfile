  
FROM pegasusdocker/deploy:submit-centos7  
  
MAINTAINER Rafael Ferreira da Silva <rafsilva@isi.edu>  
  
USER root  
  
WORKDIR /root  
RUN yum -y install git wget epel-release  
RUN yum -y groupinstall "Development Tools"  
  
# Download and install Montage  
RUN wget http://montage.ipac.caltech.edu/download/Montage_v4.0.tar.gz  
RUN tar -zxf Montage_v4.0.tar.gz  
WORKDIR /root/montage  
RUN make  
RUN cp bin/* /usr/local/bin/  
  
# Install Astropy  
RUN yum -y install python-pip python-devel  
RUN pip install astropy  
  
# Install Montage workflow  
USER tutorial  
WORKDIR /home/tutorial  
RUN git clone https://github.com/pegasus-isi/montage-workflow-v2/  
  
RUN chown -R tutorial /home/tutorial/  

