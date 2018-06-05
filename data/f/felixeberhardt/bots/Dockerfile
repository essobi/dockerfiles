FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_CTYPE C.UTF-8  
RUN apt-get update  
RUN apt-get install -y apt-utils  
  
RUN apt-get install locales  
RUN locale-gen "en_US.UTF-8"  
RUN dpkg-reconfigure locales  
  
# Install requirements for Paramiko (Cryptography) library for SFTP  
RUN apt-get install -y build-essential libssl-dev libffi-dev  
  
RUN apt-get install -y git  
  
# Install Python and Basic Python Tools  
RUN apt-get install -y python3  
RUN apt-get install -y python3-dev  
RUN apt-get install -y python3-pip  
RUN pip3 install --upgrade pip  
  
# Copy requirements from source  
COPY ./etc /requirements  
RUN pip3 install -r /requirements/requirements.txt  
  
# Install additional/optional packages  
#RUN pip3 install suds-jurko==0.6  
#RUN pip3 install paramiko==2.0.2  
#RUN pip3 install pycrypto==2.6.1  
RUN pip3 install supervisor==3.3.1  
#RUN pip3 install m3-cdecimal==2.3  
# Copy complete source  
COPY ./ /bots  
WORKDIR /bots  
  
# Install BOTS and create directories  
RUN /bots/scripts/link_python.sh  
RUN pip3 install /bots  
RUN mkdir /usr/local/lib/python3/dist-packages/bots/botssys  
RUN mkdir /usr/local/lib/python3/dist-packages/bots/botssys/sqlitedb  
RUN mkdir /dirmon  
COPY ./src/bots/install/bots.ini /usr/local/lib/python3/dist-
packages/bots/config/  
COPY ./src/bots/install/settings.py /usr/local/lib/python3/dist-
packages/bots/config/  
COPY ./src/bots/install/botsdb /usr/local/lib/python3/dist-
packages/botssys/sqlitedb/  
  
COPY ./docker/postinstall.py /bots  
  
# Install DevCron  
# failed, missing hg/mercurial : RUN pip install -e
hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
RUN pip3 install https://bitbucket.org/dbenamy/devcron/get/tip.tar.gz  
  
# Copy Supervisord.conf file  
COPY ./docker/supervisord.conf /etc/supervisor/supervisord.conf  
  
# Add Crontab file  
COPY ./docker/crontab /usr/local/lib/python3/dist-packages/bots/config/  
  
CMD /usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf  
  
EXPOSE 8080  
EXPOSE 9001  

