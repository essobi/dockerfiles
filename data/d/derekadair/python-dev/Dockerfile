FROM derekadair/python-3.4  
MAINTAINER Derek Adair "d@derekadair.com"  
# Required for pscopg2  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update -y && \  
apt-get install -y libpq-dev phantomjs xvfb firefox  
  
RUN virtualenv /env  
RUN /env/bin/pip install twine setuptools selenium==2.45.0  
RUN apt-get install -y curl  
RUN curl
https://raw.githubusercontent.com/nodesource/distributions/master/deb/setup
|bash > /dev/null 2>&1  
RUN apt-get install -y nodejs  
RUN npm install bower -g  
# cleanup  
RUN apt-get clean  

