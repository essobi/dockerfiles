# Diamond agent voor Topicus Onderwijs  
FROM ubuntu:14.04  
MAINTAINER Ralf Schimmel <ralf.schimmel@topicus.nl>, Kevin Rumbler
<kevin.rummler@topicus.nl>  
  
# Set locale  
RUN locale-gen --no-purge en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install dependencies  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y python-software-properties wget sudo net-tools  
  
RUN apt-get update  
RUN apt-get install -y vim pbuilder python-mock python-configobj python-
support cdbs python-psycopg2 git python-pip python-dev build-essential
inetutils-ping curl  
RUN pip install --upgrade pip  
RUN pip install --upgrade virtualenv  
  
RUN git clone https://github.com/topicusonderwijs/Diamond.git  
RUN pip install librato-metrics  
RUN pip install pysnmp-mibs  
RUN pip install pysnmp  
RUN pip install boto  
RUN pip install psycopg2  
  
WORKDIR /Diamond  
RUN make builddeb  
RUN sudo dpkg -i build/diamond_*_all.deb  
ADD diamond /etc/diamond/  
  
CMD []  
  
# Add start script  
ADD start.sh start.sh  
RUN chmod +x /start.sh  
  
ENTRYPOINT /start.sh  

