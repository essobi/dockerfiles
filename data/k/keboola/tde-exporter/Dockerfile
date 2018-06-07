FROM keboola/base-php56  
MAINTAINER Tomas Kacur <tomas.kacur@keboola.com>  
  
# setup the environment  
WORKDIR /tmp  
RUN yum install -y yum-plugin-ovl  
RUN yum -y install wget git tar  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install PyYaml  
RUN pip install -U pytest  
RUN pip install httplib2  
  
# prepare the container  
WORKDIR /home  
RUN git clone -b 3.4.0 --depth 1 https://github.com/keboola/tde-exporter.git
./  
WORKDIR libs  
RUN tar xvzf TDE-API-Python-Linux-64Bit.gz  
WORKDIR DataExtract-8300.15.0308.1149  
RUN python setup.py build  
RUN python setup.py install  
  
#prepare php stuff  
WORKDIR /home/php  
RUN composer install --no-interaction  
  
WORKDIR /home  
RUN PYTHONPATH=. py.test  
#remove the tests results  
RUN rm -rf /tmp/pytest-of-root/  
ENTRYPOINT python -u ./src/main.py --data=/data  

