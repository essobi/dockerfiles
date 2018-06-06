# Select source image  
FROM ubuntu:xenial  
  
# Install all dependencies  
ENV TERM linux  
  
RUN apt-get update -q  
  
RUN apt-get install -y dialog apt-utils  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get upgrade -y --no-install-recommends  
  
RUN apt-get install -y python-pip python-dev gcc  
RUN apt-get install -y apparmor apparmor-profiles apparmor-utils  
RUN apt-get install -y netcat  
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y git  
  
# required libraries  
RUN apt-get install -y libpthread-stubs0-dev  
  
RUN apt-get install -y curl  
  
RUN pip install --upgrade pip  
  
# install node  
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
RUN apt-get install -y build-essential  
  
RUN rm -rf /etc/apparmor.d/docker-engine  
  
# Install python library required  
RUN pip install git+https://github.com/OPAL-Project/codejail.git \  
&& pip install git+https://github.com/emalgorithm/bandicoot.git \  
&& pip install git+https://github.com/OPAL-Project/opalalgorithms.git \  
&& pip install python-dateutil psycopg2  
  
# Creating virtualenv for sandbox  
RUN mkdir /usr/venv  
RUN pip install virtualenv \  
&& virtualenv /usr/venv/sandbox \  
&& chmod +x /usr/venv/sandbox/bin/activate  
  
# install libraries in virtualenv  
RUN /bin/bash -c "source /usr/venv/sandbox/bin/activate \  
&& pip install git+https://github.com/emalgorithm/bandicoot.git \  
&& pip install git+https://github.com/OPAL-Project/codejail.git \  
&& pip install git+https://github.com/OPAL-Project/opalalgorithms.git \  
&& pip install python-dateutil \  
&& deactivate"  
  
WORKDIR /root  
  
# We download the opal compute  
RUN git clone -b master https://github.com/OPAL-Project/OPAL-Compute  
  
WORKDIR /root/OPAL-Compute  
  
# setup restricted environment  
RUN cp ./setupScripts/usr.venv.sandbox.bin.python /etc/apparmor.d/  
RUN cp ./setupScripts/95-sandbox /etc/sudoers.d/  
  
# create a sandbox user  
RUN useradd -ms /bin/bash sandbox  
  
RUN echo "#!/bin/bash\nsudo mount -tsecurityfs securityfs /sys/kernel/security
&& sudo apparmor_parser -r -W /etc/apparmor.d/usr.venv.sandbox.bin.python" >
/usr/bin/apparmor_init && \  
chmod +x /usr/bin/apparmor_init  
  
RUN useradd -ms /bin/bash opal  
USER opal  
  
RUN sudo ldconfig  
  
# Create app directories  
RUN mkdir -p /home/opal/app && mkdir -p /home/opal/test && mkdir -p
/home/opal/app/config  
  
# Install app dependencies  
RUN cp ./package.json /home/opal/app/  
  
# Bundle app  
RUN cp -R ./src /home/opal/app/src  
  
WORKDIR /home/opal/app  
# Install opal-compute npm dependencies  
RUN npm install --silent; exit 0;  
RUN sudo cat /root/.npm/_logs/*; exit 0;  
  
EXPOSE 80  

