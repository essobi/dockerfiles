FROM python:2  
# Add non privileged user  
RUN useradd -m user  
  
# install dependancies  
RUN apt-get update  
RUN apt-get -y install git perl nmap sslscan apache2  
  
# Install app  
RUN git clone https://github.com/golismero/golismero /usr/src/app  
WORKDIR /usr/src/app  
RUN pip install -r requirements.txt  
RUN pip install -r requirements_unix.txt  
  
# clean / optimise docker size  
RUN apt-get remove --purge -y git  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/* /var/tmp/*  
  
# running  
USER user  
ENTRYPOINT ["/usr/bin/python", "golismero.py"]  

