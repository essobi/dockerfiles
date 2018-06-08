# VERSION 0.1  
# DOCKER-VERSION 0.10.0  
# AUTHOR Saulo Alves <sauloal@gmail.com>  
# DESCRIPTION  
# TO BUILD docker build -t sauloal/mongoapistats .  
# TO UPLOAD while true; do docker push sauloal/mongoapistats; echo $?; if [ $?
== "0" ]; then exit 0; fi; done  
# TO RUN docker run -d -p 27801:8081 -p 27802:8080 -p 27803:8000 -p 27022:22
-p 27017:27017 -p 28017:28017 -p 27080:27080 --name="sauloal_mongoapistats"
sauloal/mongoapistats  
# mongo xpres mviewer fangofmongo ssh mongo mongorest mongoose  
#FROM ubuntu:14.04  
FROM sauloal/mongoapi  
  
MAINTAINER Saulo Alves <sauloal@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
  
RUN apt-get update  
  
  
#FANG OF MONGO  
#https://github.com/Fiedzia/Fang-of-Mongo  
#apt-get install -y install python-setuptools mongodb python-django python-
pymongo  
#cd fangofmongo  
#python ./manage.py runserver  
#now point your browser to http://localhost:8000/fangofmongo/ and enjoy  
#port 8000  
  
RUN apt-get install -y python-imaging python-pythonmagick python-markdown
python-textile python-docutils python-django; \  
easy_install pymongo; \  
git clone -b update https://github.com/Fiedzia/Fang-of-Mongo.git  
  
  
  
#MVIEWER  
#https://github.com/Imaginea/mViewer  
#https://github.com/downloads/Imaginea/mViewer/mViewer-v0.9.1.tar.gz  
#./start_mViewer.sh <port>  
#port 8080  
  
RUN apt-get install -y openjdk-6-jdk; \  
mkdir mViewer; cd mViewer; \  
wget -O mViewer.tar.gz
https://github.com/downloads/Imaginea/mViewer/mViewer-v0.9.1.tar.gz; \  
tar xvf mViewer.tar.gz  
  
  
  
#MONGO EXPRESS  
#http://andzdroid.github.io/mongo-express/  
#npm install -g mongo-express  
#Copy config.default.js into a new file called config.js  
#node app  
#http://localhost:8081  
#http://andzdroid.github.io/mongo-express/  
#port 8081  
  
RUN apt-get install -y nodejs npm; \  
ln -s /usr/bin/nodejs /usr/bin/node; \  
wget -O andzdroid-mongo-express.tar.gz https://github.com/andzdroid/mongo-
express/tarball/master; \  
tar xvf andzdroid-mongo-express.tar.gz; \  
cd andzdroid-mongo-express-*; \  
npm install mongodb --mongodb:native; \  
npm install express; \  
npm install mongo-express; \  
npm install underscore; \  
npm install consolidate; \  
npm install swig; \  
cp config.default.js config.js  
  
  
  
RUN locale-gen --purge en_US.UTF-8  
  
#mongo port  
EXPOSE 27017  
  
#mongo rest port  
EXPOSE 28017  
  
#mongoose port  
EXPOSE 27080  
  
#ssh port  
EXPOSE 22  
  
#fang of mongo  
EXPOSE 8000  
  
#mviewer  
EXPOSE 8080  
  
#mongo express  
EXPOSE 8081  
  
  
ADD run.sh /run.sh  
ADD fangofmongo.service.conf /etc/supervisor/conf.d/fangofmongo.service.conf  
ADD mongoexpress.service.conf /etc/supervisor/conf.d/mongoexpress.service.conf  
ADD mviewer.service.conf /etc/supervisor/conf.d/mviewer.service.conf  
  
  
#ENTRYPOINT ( /usr/sbin/sshd ) && \  
# ( /usr/bin/nohup /usr/bin/mongod --rest & ) && \  
# ( cd /Fang-of-Mongo/fangofmongo; /usr/bin/nohup /usr/bin/python manage.py
runserver 0.0.0.0:8000 & ) && \  
# ( cd /andzdroid-mongo-express-*; /usr/bin/nohup /usr/bin/npm start & ) && \  
# ( /usr/bin/nohup /usr/bin/python /sleepy.mongoose/httpd.py --xorigin & ) &&
\  
# ( cd /mViewer; /usr/bin/nohup /bin/bash /mViewer/start_mViewer.sh )  
  
  
  
#ENTRYPOINT ["bash"]  
  
#CMD "supervisor -c /etc/supervisor.conf"  
CMD /bin/bash /run.sh  
  
  
  
  
  
  
#https://gist.github.com/jpetazzo/6127116  
## this forces dpkg not to call sync() after package extraction and speeds up
install  
#RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
## we don't need and apt cache in a container  
#RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
  
  
#mongowl  
#http://mongoowl.citsoft.net/?page_id=20  
#RUN wget
https://saulo.s3.amazonaws.com/mongoowl.v.2.0.0.tgz?AWSAccessKeyId=AKIAJOWILRQECAEF7KKQ&Expires=1431178346&Signature=vrsdbyUpujQBw2ebUC75ELOONxw%3D  
#cp /download/jdk-6u35-linux-x64.bin jdkinst/  
#cd jdkinst  
#./jdkinst.sh  
#java -jar mongoowl.war  
#http://127.0.0.1:8080/mongoowl  
  
#robomongo  
#http://robomongo.org/  
#wget http://robomongo.org/files/linux/robomongo-0.8.4-x86_64.deb  
#apt-get install libgl1-mesa-glx libgl1-mesa-dev "^libxcb.*" libx11-xcb-dev
libglu1-mesa-dev libxrender-dev  
#apt-get install flex bison gperf libicu-dev libxslt-dev ruby  
#mkdir -p /usr/share/icons/  
#export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH  
#dpkg --install robomongo-0.8.4-x86_64.deb  
  
#MONGS  
#http://whit537.org/mongs/  
#git clone https://github.com/whit537/mongs.git  
#cd mongs  
#make run  

