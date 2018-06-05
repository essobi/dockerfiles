FROM python:3.4  
MAINTAINER Scott McCloud <scott.m.mccloud@gmail.com>  
  
VOLUME /config  
  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app/appdaemon  
WORKDIR /usr/src/app  
  
RUN pip3 install --no-cache-dir colorlog cython  
  
# For the nmap tracker, bluetooth tracker, Z-Wave  
RUN apt-get update && \  
apt-get install -y --no-install-recommends nmap net-tools cython3 libudev-dev
sudo libglib2.0-dev git && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY build_python_openzwave script/build_python_openzwave  
RUN chmod +x script/build_python_openzwave && \  
script/build_python_openzwave && \  
mkdir -p /usr/local/share/python-openzwave && \  
ln -sf /usr/src/app/build/python-openzwave/openzwave/config
/usr/local/share/python-openzwave/config  
  
ADD https://raw.githubusercontent.com/home-assistant/home-
assistant/dev/requirements_all.txt requirements_all.txt  
# certifi breaks Debian based installs  
RUN pip3 install --no-cache-dir -r requirements_all.txt && pip3 uninstall -y
certifi && \  
pip3 install mysqlclient psycopg2 && \  
pip3 install daemonize sseclient configparser astral # this line is for
AppDaemon  
  
# Copy source  
RUN git clone https://github.com/home-assistant/home-assistant.git tmp && mv
tmp/.git . && rm -rf tmp && git reset --hard  
RUN git clone https://github.com/acockburn/appdaemon.git tmp && mv tmp/*
appdaemon/ && rm -rf tmp  
  
CMD [ "python", "-m", "homeassistant", "--config", "/config", ";",
"./appdaemon/bin/appdaemon.py", "appdaemon/conf/examples.cfg" ]  

