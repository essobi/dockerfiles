FROM python:3.6  
# File Author / Maintainer  
MAINTAINER Jrgen Blakstad  
  
# Update the sources list  
RUN apt-get update  
  
RUN apt-get install -y apt-utils  
  
# Install basic applications  
RUN apt-get install -y vim tar git curl nano wget net-tools build-essential
telnet openssh-client less netcat nmap  
  
# Install python git libraries  
RUN pip install gitdb  
RUN pip install nose  
RUN pip install -U mock  
RUN pip install gitpython  
  
# Install Netmiko  
# https://pynet.twb-tech.com/blog/automation/netmiko.html  
RUN apt-get install -y libffi-dev libssl-dev python-yaml  
RUN pip install pycrypto  
RUN pip install utils  
RUN pip install --upgrade cffi  
RUN pip install --upgrade cryptography  
RUN pip install netmiko  
  
# Install node 7  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g npm-autoinit  
RUN npm config set onload-script npm-autoinit/autoinit  
  
# Install ciscoparse  
# https://www.npmjs.com/package/ciscoparse  
RUN npm install ciscoparse  
  
# Install ciscoconfparse (Python tool to parse cisco config)  
RUN pip install --upgrade ciscoconfparse  
  
# Install django  
RUN pip install django  
RUN pip install dj-static  
RUN pip install static3  
RUN pip install wheel  
  
# Install redis, celery  
RUN apt-get -y install redis-server  
RUN service redis-server start  
RUN pip install celery[redis]  
RUN pip install django-celery-results  
  
# Install Butterfly (xterm in browser)  
RUN pip install butterfly  
RUN pip install libsass  
  
# Install openssh  
RUN apt-get -y install openssh-server  
RUN perl -pi -e 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
  
# Install filebrowser  
RUN pip install django-grappelli  
RUN pip install Pillow  
RUN pip install django-tinymce  
RUN pip install django-filebrowser  
  
# Import MongoDB public GPG key AND create a MongoDB list file  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/debian $(lsb_release -a | grep
Codename: | awk '{print $2}')/mongodb-org/3.2 main" | tee
/etc/apt/sources.list.d/mongodb-org-3.2.list  
  
# Update apt-get sources AND install MongoDB  
RUN apt-get update && apt-get install -y mongodb-org  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
# Install vis.js for network map visualize  
RUN npm install vis  
  
# Install jedha for cdp parsing  
RUN pip install --upgrade jedha  
  
# Install Ansible  
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367  
RUN apt-get update  
RUN apt-get install -y ansible  
RUN pip install ansible  
  
# Install ntc-ansible  
RUN perl -pi -e 's/#inventory/inventory/g' /etc/ansible/ansible.cfg  
RUN perl -pi -e 's/#library/library/g' /etc/ansible/ansible.cfg  
RUN mkdir -p /usr/share/my_modules/  
RUN cd /usr/share/my_modules/ && git clone
https://github.com/networktocode/ntc-ansible --recursive  
RUN pip install jtextfsm  
RUN pip install terminal  
RUN 2to3 -w /usr/local/lib/python3.6/site-packages/texttable.py  
  
# Install Napalm  
RUN pip install napalm  
  
# Install django-netjsongraph  
RUN pip install django-netjsongraph  
  
# Install dateutils  
RUN pip install python-dateutil  
  
# Install Graphviz  
RUN apt-get -y install libssh2-1-dev  
RUN apt-get -y install graphviz  
RUN apt-get -y install graphviz-dev  
  
# Install some perl packages  
RUN (echo y;echo o conf prerequisites_policy follow;echo o conf commit)|cpan  
RUN perl -MCPAN -e 'install Net::SSLeay'  
RUN perl -MCPAN -e 'install LWP::Protocol::https'  
RUN perl -MCPAN -e 'install XML::LibXML'  
RUN perl -MCPAN -e 'install JSON'  
RUN perl -MCPAN -e 'install Net::SSH2'  
RUN perl -MCPAN -e 'install Net::Telnet'  
RUN perl -MCPAN -e 'install autovivification'  
RUN perl -MCPAN -e 'install XML::Simple'  
RUN perl -MCPAN -e 'install GraphViz2'  
RUN cpan -i MONGODB/MongoDB-v0.708.4.0.tar.gz  
  
# Install additional django modules and mongoDB modules  
RUN pip install pymongo  
RUN pip install django-crispy-forms  
RUN pip install django-braces  
  
ENTRYPOINT service redis-server start && bash  
  
EXPOSE 80 22 57575  

