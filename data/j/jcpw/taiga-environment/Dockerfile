FROM ubuntu:14.04  
MAINTAINER neuhaus.julian@gmail.com  
  
RUN apt-get update && apt-get install -y \  
sudo \  
build-essential binutils-doc autoconf flex bison libjpeg-dev \  
libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev \  
automake libtool libffi-dev curl git tmux gettext \  
python3 python3-pip python-dev python3-dev python-pip virtualenvwrapper \  
libxml2-dev libxslt-dev \  
libpq-dev \  
nginx \  
gunicorn \  
postgresql-9.3 postgresql-contrib-9.3 \  
postgresql-doc-9.3 postgresql-server-dev-9.3 && \  
pip3 install circus  
  
RUN adduser taiga  
  
USER taiga  
  
RUN cd /home/taiga && git clone https://github.com/taigaio/taiga-back.git
taiga-back && \  
cd taiga-back && \  
git checkout stable && \  
cd /home/taiga && \  
git clone https://github.com/taigaio/taiga-front-dist.git taiga-front-dist &&
\  
cd taiga-front-dist && \  
git checkout stable  
  
USER root  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
USER taiga  
  
  
RUN echo 'export WORKON_HOME=/home/taiga/.virtualenvs' >> /home/taiga/.bashrc
&& \  
echo 'source /usr/share/virtualenvwrapper/virtualenvwrapper.sh' >>
/home/taiga/.bashrc  
  
RUN source /usr/share/virtualenvwrapper/virtualenvwrapper.sh && \  
mkvirtualenv -p /usr/bin/python3.4 taiga && \  
workon taiga && \  
cd /home/taiga/taiga-back && \  
pip install -r requirements.txt  
  
USER root  
RUN service postgresql start && \  
sudo -u postgres createuser taiga && \  
sudo -u postgres createdb taiga -O taiga && \  
echo 'taiga ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
  
USER taiga  
RUN sudo service postgresql start && \  
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh && \  
workon taiga && \  
  
cd /home/taiga/taiga-back && \  
python manage.py migrate --noinput && \  
python manage.py loaddata initial_user && \  
python manage.py loaddata initial_project_templates && \  
python manage.py loaddata initial_role && \  
python manage.py compilemessages && \  
python manage.py collectstatic --noinput  
  
USER root  
  
ADD circus.ini /  
ADD circus.conf /  
ADD nginx_taiga /  
ADD launchscript /  
  
RUN mkdir -p /tmp/  
ADD local.py.tmpl /tmp/  
ADD app-loader.js.tmpl /tmp/  
ADD conf.json.tmpl /tmp/  
  
RUN chmod +x launchscript  
  
RUN mkdir -p cd /home/taiga/conf/ && \  
mkdir /home/taiga/logs && \  
mv circus.ini /home/taiga/conf && \  
mv circus.conf /etc/init && \  
mv nginx_taiga /etc/nginx/sites-available/taiga && \  
chown -R taiga:taiga /home/taiga  
  
RUN sudo rm /etc/nginx/sites-enabled/default && \  
sudo ln -s /etc/nginx/sites-available/taiga /etc/nginx/sites-enabled/taiga  
  
EXPOSE 80 5432  
CMD /launchscript && service nginx restart && service postgresql start &&
/usr/local/bin/circusd /home/taiga/conf/circus.ini  
  

