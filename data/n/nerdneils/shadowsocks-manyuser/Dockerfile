FROM ubuntu:14.04  
MAINTAINER nerdneils <dengqi935@outlook.com>  
  
RUN apt-get update && apt-get -y install language-pack-en  
RUN apt-get -y install build-essential python python-dev python-pip git
python-m2crypto  
RUN pip install cymysql  
RUN git clone -b manyuser https://github.com/mengskysama/shadowsocks.git
/manyusers  
RUN apt-get install -y supervisor  
RUN apt-get clean && \  
rm -rf /var/lib/apt/list/*  
COPY supervisor.conf /etc/supervisor/conf.d/  
COPY Config.py /manyusers/shadowsocks/  
WORKDIR /manyusers/shadowsocks/  
  
CMD ['supervisor','-n']

