FROM racker/precise-with-updates:latest  
RUN apt-get update  
RUN apt-get install -y sysstat vim mtr-tiny nmap wget git python-setuptools
python-dev build-essential  
RUN easy_install pip  
RUN pip install rackspace-novaclient  
RUN git clone git://github.com/gholt/swiftly.git  
RUN git clone https://github.com/major/supernova.git  
RUN git clone https://github.com/cloudnull/turbolift.git  
RUN cd swiftly && python setup.py install  
RUN cd supernova && python setup.py install  
RUN cd turbolift && python setup.py install  
RUN touch ~/.supernova  
RUN echo "[region]" >> ~/.supernova  
RUN echo "OS_AUTH_URL=https://identity.api.rackspacecloud.com/v2.0/" >>
~/.supernova  
RUN echo "OS_USERNAME=<USERNAME>" >> ~/.supernova  
RUN echo "OS_PASSWORD=<APIKEY>" >> ~/.supernova  
RUN echo "OS_TENANT_NAME=<DDI>" >> ~/.supernova  
RUN echo "OS_AUTH_SYSTEM=rackspace" >> ~/.supernova  
RUN echo "OS_REGION_NAME=DFW" >> ~/.supernova  
RUN echo "NOVA_SERVICE_NAME=cloudServersOpenStack" >> ~/.supernova  
RUN echo "OS_PROJECT_ID=nova" >> ~/.supernova  
RUN head -1 .supernova  
ENV HOME /

