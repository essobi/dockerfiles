FROM ubuntu:16.04  
MAINTAINER Ellis Percival <docker-tradedangerous@failcode.co.uk>  
  
RUN apt-get -q -y update  
RUN apt-get -q -y install python3 python3-dev python3-setuptools git sqlite3  
RUN easy_install3 pip  
RUN pip3 install --upgrade setuptools requests  
RUN cd /opt && git clone https://bitbucket.org/kfsone/tradedangerous.git  
VOLUME /opt/tradedangerous/data  
  
ENTRYPOINT ["python3", "/opt/tradedangerous/trade.py"]  
CMD ["import", "--plug=maddavo", "-O=csvs"]  

