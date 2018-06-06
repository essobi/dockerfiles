FROM jenkins  
USER root  
RUN apt-get update && apt-get install -y python-pip python-dev build-essential
&& pip install virtualenv  
COPY requirements.txt /usr/share/jenkins/requirements.txt  
RUN virtualenv /usr/share/jenkins/delphix && bash -c "source
/usr/share/jenkins/delphix/bin/activate && pip install --upgrade -r
/usr/share/jenkins/requirements.txt" && chown -R jenkins.jenkins
/usr/share/jenkins/delphix  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

