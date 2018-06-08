# Pull base image.  
FROM ubuntu:14.04.4  
# Set the author  
MAINTAINER Chakkrit Termritthikun <chakkritte57@nu.ac.th>  
  
# Install Nginx.  
RUN \  
apt-get -q -y update && \  
apt-get -q -y install python2.7 python2.7-dev \  
wget software-properties-common pgp unzip nano git  
  
RUN \  
add-apt-repository ppa:nginx/stable && \  
  
wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | sudo apt-key add \- && \  
echo deb http://dl.hhvm.com/ubuntu trusty main | sudo tee
/etc/apt/sources.list.d/hhvm.list  
  
RUN \  
apt-get -q -y update && \  
apt-get -q -y install hhvm nginx  
  
RUN \  
update-rc.d hhvm defaults && \  
/usr/share/hhvm/install_fastcgi.sh && \  
/etc/init.d/nginx restart && \  
/etc/init.d/hhvm restart  
  
RUN cd /root && \  
git clone https://github.com/tyiannak/pyAudioAnalysis.git  
  
RUN cd /root && \  
export PYTHONPATH=$PYTHONPATH:"/root"  
  
RUN cd /root && \  
apt-get -q -y install python-numpy python-matplotlib \  
python-scipy libgsl0-dev  
  
RUN \  
wget https://dl.dropboxusercontent.com/u/63724881/Face/mlpy-3.5.0.tar.gz && \  
#wget
http://sourceforge.net/projects/mlpy/files/mlpy%203.5.0/mlpy-3.5.0.tar.gz && \  
tar xvf mlpy-3.5.0.tar.gz && \  
cd mlpy-3.5.0 && \  
python setup.py install  
  
RUN apt-get -q -y install python-sklearn python-pip  
  
RUN cd /var/www/html/ && \  
echo "<?php\n phpinfo();" > /var/www/html/info.php  
  
#RUN cd /root && \  
# wget https://dl.dropboxusercontent.com/u/63724881/audio.zip && \  
# unzip audio.zip  
RUN \  
pip install eyeD3 && \  
pip install scikits.talkbox  
  
#RUN cd /var/www/html && \  
# wget https://dl.dropboxusercontent.com/u/63724881/audio.zip && \  
# unzip audio.zip  
# wget https://dl.dropboxusercontent.com/u/63724881/audios.zip && \  
# unzip audios.zip  
RUN cd /var/www/html && \  
# wget https://dl.dropboxusercontent.com/u/63724881/audio.zip  
wget https://dl.dropboxusercontent.com/u/63724881/Face/data4.zip  
# unzip audio.zip  
# wget https://dl.dropboxusercontent.com/u/63724881/audios.zip && \  
# unzip audios.zip  
#ADD audio.zip /var/www/html/audio.zip  
ADD train.py /root/train.py  
  
RUN cd /var/www/html && \  
unzip data4.zip && \  
python /root/train.py  
  
RUN \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
ADD default /etc/nginx/sites-available/default  
  
RUN mkdir /var/www/html/uploads  
  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  
#RUN mkdir -p /var/www/html/uploads/  
ADD UploadToServer.php /var/www/html/UploadToServer.php  
  
# Boot up Nginx, and HHVM when container is started  
CMD service hhvm start && nginx  

