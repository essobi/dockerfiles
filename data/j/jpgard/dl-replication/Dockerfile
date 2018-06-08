# Pull base image.  
FROM ubuntu:16.04  
# install, sklearn, keras, and depends  
RUN \  
apt-get update && \  
apt-get install -y sudo software-properties-common python-software-properties
&& \  
apt-get -y install python3-dev python3-pip python-virtualenv python-numpy
python-scipy libatlas-dev libatlas3-base libhdf5-dev && \  
rm -rf /var/lib/apt/lists/* && \  
pip3 install pandas keras && \  
update-alternatives --set libblas.so.3 /usr/lib/atlas-base/atlas/libblas.so.3
&& \  
update-alternatives --set liblapack.so.3 /usr/lib/atlas-
base/atlas/liblapack.so.3 && \  
pip3 install -U scikit-learn && \  
pip3 install tensorflow h5py cython && \  
# install MySQL and add configurations  
echo "mysql-server-5.7 mysql-server/root_password password root" | sudo
debconf-set-selections && \  
echo "mysql-server-5.7 mysql-server/root_password_again password root" | sudo
debconf-set-selections && \  
sudo apt-get -y update && \  
sudo apt-get -y dist-upgrade && \  
apt-get -y install mysql-server-5.7 && \  
echo "secure-file-priv = \"\"" >> /etc/mysql/mysql.conf.d/mysqld.cnf  
  
# add scripts  
ADD dl_replication.py /  
ADD feature_extraction feature_extraction  
ADD modeling modeling  
  
# define entrypoint  
ENTRYPOINT ["python3", "dl_replication.py"]

