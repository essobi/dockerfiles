FROM ubuntu:17.10  
  
WORKDIR /tmp  
  
# Install Python 3.6  
RUN apt-get update \  
&& apt-get install -y \  
python3.6 \  
python3-pip \  
unixodbc-dev \  
&& pip3 install cheesefactory \  
&& apt-get remove --auto-remove -y \  
python3-pip \  
unixodbc-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc/* \  
&& rm -rf /usr/share/man/* \  
&& ln -s /usr/bin/python3.6 /usr/bin/python  
  
# Copy and configure app  
#COPY app/. /app  
#RUN mkdir -p /etc/crontabs  
#COPY crontab /etc/crontabs/root  
#RUN cat crontab > /etc/crontabs/root  
#ENTRYPOINT ["/bin/sh"]  

