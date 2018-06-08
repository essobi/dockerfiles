FROM ubuntu:14.04  
MAINTAINER Alexander Skjolden alex@plastboks.net  
  
RUN apt-get update  
#RUN apt-get upgrade  
RUN apt-get -y install build-essential  
RUN apt-get -y install git  
RUN apt-get -y install python-virtualenv  
RUN apt-get -y install python2.7-dev  
RUN apt-get -y install virtualenvwrapper  
  
VOLUME /pyrtos/shared  
  
RUN mkdir -p /opt/virtualenvs  
WORKDIR /opt/virtualenvs  
RUN git clone https://github.com/plastboks/Pyrtos.git app  
WORKDIR /opt/virtualenvs/app  
RUN pip install -e .  
RUN /usr/local/bin/initialize_pyrtos_db autogenerate.ini  
  
EXPOSE 6543  
USER daemon  
ENTRYPOINT ["/usr/local/bin/pserve"]  

