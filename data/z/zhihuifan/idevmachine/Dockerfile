from mikaelhg/docker-rabbitmq  
  
RUN apt-get update && apt-get install -y software-properties-common && \  
apt-get update && \  
apt-add-repository ppa:ubuntu-elisp/ppa -y && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get update && \  
apt-get install -y --force-yes pwgen mongodb-org mongodb-org-server mongodb-
org-shell mongodb-org-mongos mongodb-org-tools && \  
apt-get install -y python3-lxml sqlite3 screen telnet && \  
apt-get update && \  
apt-get install -y \  
python \  
python-dev \  
python3-pip \  
git \  
emacs-snapshot \  
gdb \  
python3-pep8 \  
python3-scipy \  
vim && \  
pip3 install ipython \  
jedi \  
autopep8 \  
xlrd \  
importmagic \  
yapf \  
django-celery \  
flower \  
beautifulsoup4 \  
pylint \  
django \  
celery \  
pandas \  
pandas-datareader \  
pymongo \  
scikit-learn \  
elasticsearch  
COPY .emacs /root/  
COPY .pylintrc /root/  
COPY basic.sh /root/  
RUN pip3 install tushare sqlalchemy  
COPY .bash_profile /root/  
ENV IPY_TEST_SIMPLE_PROMP 1  
  
RUN pip3 install tox pytest pytest-xdist

