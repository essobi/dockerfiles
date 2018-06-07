FROM python:2.7  
RUN pip install splinter nose && \  
# Install PhantomJS.  
apt-get install -qqy curl && \  
curl -sL https://deb.nodesource.com/setup_5.x | bash - && \  
apt-get install -qqy nodejs build-essential && \  
npm install -g phantomjs  
  
WORKDIR /test/  
  
CMD ["nosetests"]  

