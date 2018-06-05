  
# Id: docker-jenkins-mpe/0.0.2-dev  
FROM evarga/jenkins-slave  
  
  
RUN mkdir /home/jenkins/workspace  
RUN chown jenkins:jenkins /home/jenkins/workspace  
  
RUN apt-get update -qq && apt-get install -qqy \  
git git-annex rsync make  
  
RUN mkdir -vp /src/  
RUN chgrp staff /src /srv /usr/local/bin  
RUN chmod g+rw /src /srv /usr/local/bin  
  
# Intall BATS  
RUN git clone https://github.com/sstephenson/bats.git /src/bats  
RUN /src/bats/install.sh /usr/local  
  
# Install PIP  
RUN curl https://bootstrap.pypa.io/get-pip.py -o /src/get-pip.py  
RUN python /src/get-pip.py  
# run pip install later as user  
#RUN pip install virtualenv  
RUN pip install setuptools virtualenv zope.component zope.interface sqlalchemy
sqlalchemy-migrate  
  
# :vim:ft=Dockerfile:  

