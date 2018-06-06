FROM ubuntu:14.04  
MAINTAINER <support@collectiveacuity.com>  
  
# Standard OS Utils  
RUN apt-get update  
RUN apt-get --fix-missing install -y python  
RUN apt-get install -y build-essential  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y libffi-dev  
RUN apt-get install -y python-dev  
RUN apt-get install -y python3-pip  
RUN apt-get install -y wget  
RUN apt-get install -y unzip  
RUN apt-get install -y curl  
  
# Install PhantomJS  
RUN apt-get install -y libfontconfig  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar -xvf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN rm phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN mv phantomjs-2.1.1-linux-x86_64 /home/phantomjs  
ENV PATH $PATH:/home/phantomjs/bin  
  
# Install Ngrok  
RUN wget https://dl.ngrok.com/ngrok_2.0.19_linux_amd64.zip  
RUN unzip ngrok_2.0.19_linux_amd64.zip  
RUN rm ngrok_2.0.19_linux_amd64.zip  
RUN mkdir /home/ngrok  
RUN mv ngrok /home/ngrok/ngrok  
ENV PATH $PATH:/home/ngrok  
  
# Install Node, NPM & LocalTunnel  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN apt-get install -y nodejs  
RUN npm install -g npm  
RUN npm install -g localtunnel  
  
# Python Dependencies  
RUN pip3 install python-dateutil  
RUN pip3 install pytz  
RUN pip3 install tzlocal  
RUN pip3 install mandrill  
RUN pip3 install twilio  
RUN pip3 install flask  
RUN pip3 install boto3  
RUN pip3 install pysha3  
RUN pip3 install cryptography  
RUN pip3 install paramiko  
RUN pip3 install scp  
RUN pip3 install pytest  
RUN pip3 install gunicorn  
RUN pip3 install textblob  
RUN pip3 install cassandra-driver  
RUN pip3 install dropbox  
RUN pip3 install PyDrive  
RUN pip3 install selenium  
RUN pip3 install splinter  
  
# Install Lab Modules  
COPY imports/labpack-0.1.0.tar.gz /labpack-0.1.0.tar.gz  
RUN tar -xvf labpack-0.1.0.tar.gz  
RUN rm labpack-0.1.0.tar.gz  
RUN cd labpack-0.1.0; python3 setup.py install; cd /  
  
# Initiate Flask on Gunicorn  
# CMD ["gunicorn": "--chdir server -w 3 launch:app -b 0.0.0.0:5000"]

