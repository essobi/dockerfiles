FROM ubuntu  
ENV GIT_REV develop  
ENV CLOTO_SETTINGS_FILE /etc/fiware.d/fiware-cloto.cfg  
RUN apt-get update  
RUN apt-get -y install python-dev \  
libpq-dev libmysqlclient-dev libpq-dev \  
git curl libffi-dev zip python-mysqldb\  
supervisor netcat python-clips build-essential gcc  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"  
RUN python get-pip.py  
RUN git clone https://github.com/telefonicaid/fiware-cloto /opt/fiware-cloto  
WORKDIR /opt/fiware-cloto  
RUN git checkout ${GIT_REV}  
RUN mkdir /etc/fiware.d/  
RUN mkdir /var/log/fiware-cloto  
RUN pip install -r requirements.txt  
COPY fiware-cloto.cfg /etc/fiware.d/fiware-cloto.cfg  
RUN cp utils/cloto_start /etc/fiware.d/  
RUN chmod a+x /etc/fiware.d/cloto_start  
RUN cp utils/fiware-cloto.conf /etc/supervisor/conf.d  
COPY start.sh start.sh  
CMD ./start.sh  

