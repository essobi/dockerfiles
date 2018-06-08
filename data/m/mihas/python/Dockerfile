FROM mihas/civic-baseimage  
  
RUN apt-get update && apt-get -y install \  
python-pil \  
git \  
gdal-bin \  
python-gdal \  
libxml2-dev libxslt1-dev \  
libpq-dev \  
libjpeg-dev \  
python-virtualenv \  
python-dev \  
python-setuptools \  
python-pip  
  
RUN easy_install pip==7.1.2 && pip install ipython pudb  
  
#=================================  
# Python PIP packages  
ADD ./requirements.txt .  
RUN pip install -r requirements.txt  
#=================================  
#=====================================  
# SSH  
#=====================================  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
#=====================================  
EXPOSE 8000  
RUN mkdir /var/log/civic && chmod -R 777 /var/log/civic  

