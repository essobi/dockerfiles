FROM ubuntu:14.04  
# Install pre-requisites.  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
python-pip \  
python-dev \  
python-lxml \  
swig \  
\--no-install-recommends  
  
RUN rm -rf /var/lib/apt/lists/* \  
&& cd /usr/include/openssl/ \  
&& ln -s ../x86_64-linux-gnu/openssl/opensslconf.h . \  
&& pip install cherrypy lxml mako M2Crypto netaddr  
  
# Create a dedicated/non-privileged user to run the app.  
RUN addgroup spiderfoot && \  
useradd -r -g spiderfoot -d /home/spiderfoot -s /sbin/nologin -c "SpiderFoot
User" spiderfoot  
  
ENV SPIDERFOOT_VERSION 2.6.1  
# Download the specified release.  
RUN git clone https://github.com/smicallef/spiderfoot.git /home/spiderfoot &&
\  
chown -R spiderfoot:spiderfoot /home/spiderfoot && \  
cd /home/spiderfoot && \  
git checkout v${SPIDERFOOT_VERSION}-final  
WORKDIR /home/spiderfoot  
  
USER spiderfoot  
WORKDIR /home/spiderfoot  
  
EXPOSE 8080  
# Run the application.  
ENTRYPOINT ["/usr/bin/python"]  
CMD ["sf.py", "0.0.0.0:8080"]  

