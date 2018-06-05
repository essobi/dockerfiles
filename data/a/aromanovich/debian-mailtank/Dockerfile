FROM aromanovich/debian:wheezy  
RUN apt-get update -y  
RUN apt-get install -y sudo git openssh-client bash apt-utils dialog  
RUN apt-get install -y python python-dev python-pip  
RUN apt-get install -y mysql-server mysql-client libmysqlclient-dev  
RUN echo "%admin ALL=NOPASSWD:ALL" >> /etc/sudoers  
# Mailtank-specific dependencies:  
RUN apt-get -y install zlib1g-dev libevent-dev gfortran libopenblas-dev
liblapack-dev  
RUN apt-get -y install python-numpy python-scipy  
RUN easy_install -U distribute  
RUN apt-get -y install pkg-config graphviz-dev libxml2-dev libxslt-dev  
RUN pip install nltk==2.0.4 scikit-learn==0.14.1  
ADD ./requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
RUN rm /tmp/requirements.txt

