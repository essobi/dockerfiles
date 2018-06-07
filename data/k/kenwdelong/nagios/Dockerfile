FROM jasonrivers/nagios:4.3.2  
MAINTAINER kenwdelong@yahoo.com  
RUN apt-get \--yes install python &&\  
apt-get clean all  
RUN echo 'SetEnv TZ "America/Los_Angeles"' >> /etc/apache2/conf-
enabled/nagios.conf  
RUN wget https://bootstrap.pypa.io/get-pip.py &&\  
python get-pip.py &&\  
rm get-pip.py &&\  
pip install boto tornado  

