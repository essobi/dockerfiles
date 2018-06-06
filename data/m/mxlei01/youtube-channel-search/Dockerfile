FROM buildpack-deps:wheezy  
  
#=====Create a folder, and copy our application into the application
folder====  
RUN mkdir /application  
COPY Tornado-Application /application/Tornado-Application  
COPY MongoDB-Settings /application/MongoDB-Settings  
COPY MeteorJS-Application /application/MeteorJS-Application  
COPY Build-Scripts /application/Build-Scripts  
COPY .coveragerc /application/  
RUN apt-get install -y git  
COPY .git /application  
#=====Create a folder, and copy our application into the application
folder====  
#===========================Start Update
Debian================================  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install apt-utils  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install build-essential python-dev  
RUN apt-get -y install ca-certificates  
#===========================End Update
Debian==================================  
#===========================Install
Tornado/PyMongo/Motor======================  
RUN apt-get -y install python-pip  
RUN pip install -r /application/Tornado-Application/requirements.txt  
#===========================Install
Tornado/PyMongo/Motor======================  
#===========================Installing
MeteorJS================================  
RUN curl https://install.meteor.com/ | sh  
#===========================Installing
MeteorJS================================  
#===========================Installing
MongoDB=================================  
RUN curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.0.6.tgz  
RUN mkdir MongoDB  
RUN tar -C ./MongoDB -zxvf mongodb-linux-x86_64-3.0.6.tgz  
RUN mkdir /MongoDB/mongodb-linux-x86_64-3.0.6/.data  
#===========================Installing
MongoDB=================================  
#===========================Installing
Supervisord=============================  
RUN apt-get install -y supervisor  
#===========================Installing
Supervisord=============================  
#===========================Installing
PS======================================  
RUN apt-get install -y procps  
#===========================Installing
PS======================================  
#===========================Installing
NodeJS==================================  
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install --yes nodejs  
#===========================Installing
NodeJS==================================  
#===========================Installing
demeteorizer============================  
RUN npm install -y -g demeteorizer  
#===========================Installing
demeteorizer============================  
#===========================Expose
Ports=======================================  
# MeteorJS  
EXPOSE 3000  
# HTTP and HTTPS  
EXPOSE 80  
EXPOSE 443  
#===========================Expose
Ports=======================================  
#===========================Create the application in meteorJS
folder==========  
RUN cd /application/MeteorJS-Application && meteor create . && meteor remove
insecure && meteor remove autopublish && demeteorizer  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh | bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN cd /application/MeteorJS-Application/.demeteorized/bundle/programs/server
&& source ~/.nvm/nvm.sh && nvm install 0.10.40 && nvm use 0.10.40 && npm
install  
#===========================Create the application in meteorJS
folder==========  
#===========================Run
Supervisord====================================  
COPY Supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN mkdir /var/supervisord  
CMD /usr/bin/supervisord  
#===========================Run
Supervisord====================================  

