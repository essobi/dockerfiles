FROM python:3.6  
RUN wget -q
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
tar -xjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \  
mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin && \  
rm -rf phantomjs-2.1.1-linux-x86_64.tar.bz2 phantomjs-2.1.1-linux-x86_64  
ENV TERM xterm  
ENV SCRAPY_SETTINGS_MODULE rslinkedin.settings  
ENV RS_LKD_USERNAME pcastrotigre@gmail.com  
ENV RS_LKD_PASSWORD xxxxx  
RUN mkdir -p /app  
WORKDIR /app  
COPY ./requirements.txt /app/requirements.txt  
RUN pip install --no-cache-dir -r requirements.txt  
COPY . /app  
RUN python setup.py install  

