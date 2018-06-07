FROM ubuntu:latest  
MAINTAINER Dan Budris <dbudris@bu.edu>  
  
RUN apt-get update -y  
RUN apt-get install -y \  
python2.7 \  
python-pip \  
curl \  
wget \  
git \  
libncurses5-dev \  
sqlite3 \  
nodejs-legacy \  
node.js \  
npm \  
&& pip install virtualenv  
  
# make the base directories  
RUN mkdir ~/g1 && mkdir ~/g1/source/  
  
# clone the git repository to local  
RUN git clone https://github.com/danbudris/BU_MET_CS673.git ~/g1/source  
  
# create the virtual environment and run the setup and database migration
scripts  
RUN virtualenv -p /usr/bin/python2.7 ~/g1/virtualenv && cd ~/g1/source/group1
&& ../../virtualenv/bin/pip install -r ../requirements.txt  
  
RUN mkdir ~/g1/source/database  
  
RUN cd ~/g1/source/group1 && ../../virtualenv/bin/python manage.py
makemigrations  
  
RUN cd ~/g1/source/group1 && ../../virtualenv/bin/python manage.py migrate  
  
# create a basic superuser account for use in debugging and development  
RUN cd ~/g1/source/group1 && echo "from django.contrib.auth.models import
User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" |
../../virtualenv/bin/python manage.py shell  
  
RUN cd ~/g1/source/group1/communication/node && npm install morgan && npm
install fs-extra  
  
COPY run.sh /opt/  
  
EXPOSE 8000  
EXPOSE 80  
EXPOSE 3000  
CMD
["/root/g1/virtualenv/bin/python","/root/g1/source/group1/manage.py","runserver","0.0.0.0:8000"]  

