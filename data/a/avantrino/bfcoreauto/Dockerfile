FROM ubuntu:trusty  
  
MAINTAINER bluefish-team  
  
#create a directory for Workdir  
RUN mkdir /mybluefish  
  
#From now on all operations will happen from here  
WORKDIR /mybluefish  
  
#Update the mongodb3.4 repo details and respective public key  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu
trusty/mongodb-org/3.4 multiverse" > /etc/apt/sources.list.d/mongodb-
org-3.4.list  
  
#Updates the repository packages list and Install required dependencies  
#Install Python dependencies  
#Install Other dependencies  
#Install Python Pandas  
#Install Database related dependencies  
RUN apt-get update && apt-get install -y atop build-essential cython cython3
gcc git gfortran lib32z1-dev libatlas-base-dev \  
libcups2-dev libcurl4-gnutls-dev libffi-dev libmysqlclient-dev libpq-dev
librtmp-dev libssl-dev \  
libxml2-dev libxslt1-dev lsof ltrace mongodb-org-shell mongodb-org-tools
mysql-client \  
openssh-server p7zip-full postgresql-client pstack \  
python2.7 python-dev python-distribute python-matplotlib python-mysqldb
python-numpy python-pandas \  
python-scipy python-setuptools python-statsmodels python-tables \  
redis-tools rsync snmp sqlite3 sshpass strace unzip valgrind \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
#Install latest version of pip  
RUN easy_install -U pip  
RUN easy_install -U statsmodels  
RUN pip install -U setuptools  
RUN git config --global http.sslVerify false && pip install -U
git+http://github.com/Eugeny/celery#egg=celery==4.0.2.1  
  
#Copy Python dependencies, Note that any PATH is relative to Context Directory  
#Install Python dependencies, Note that any PATH is relative to WORKDIR  
ADD requirements-caps.txt /mybluefish/requirements-caps.txt  
ADD requirements-abc.txt /mybluefish/requirements-abc.txt  
ADD requirements-def.txt /mybluefish/requirements-def.txt  
ADD requirements-ghi.txt /mybluefish/requirements-ghi.txt  
ADD requirements-jkl.txt /mybluefish/requirements-jkl.txt  
ADD requirements-mno.txt /mybluefish/requirements-mno.txt  
ADD requirements-pqr.txt /mybluefish/requirements-pqr.txt  
ADD requirements-stu.txt /mybluefish/requirements-stu.txt  
ADD requirements-vwxyz.txt /mybluefish/requirements-vwxyz.txt  
RUN pip install -r requirements-caps.txt  
RUN pip install -r requirements-abc.txt  
RUN pip install -r requirements-def.txt  
RUN pip install -r requirements-ghi.txt  
RUN pip install -r requirements-jkl.txt  
RUN pip install -r requirements-mno.txt  
RUN pip install -r requirements-pqr.txt  
RUN pip install -r requirements-stu.txt  
RUN pip install -r requirements-vwxyz.txt  
  
CMD ["/bin/true"]  

