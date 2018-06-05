FROM ubuntu:14.04  
  
MAINTAINER Berry Goudswaard <berry@noregression.nl>  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
build-essential binutils-doc autoconf flex bison libjpeg-dev \  
libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev \  
automake libtool libffi-dev curl git tmux gettext \  
postgresql-server-dev-9.3 \  
python3 python3-pip python-dev python3-dev python-pip virtualenvwrapper \  
libxml2-dev libxslt-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -G sudo -d /home/taiga -m taiga \  
&& sed -i.bkp -e 's/%sudo\s\\+ALL=(ALL\\(:ALL\\)\?)\s\\+ALL/%sudo
ALL=NOPASSWD:ALL/g' /etc/sudoers \  
&& cd /usr/bin \  
&& rm easy_install \  
&& rm pydoc \  
&& rm python \  
&& rm python-config \  
&& ln -s easy_install-3.5 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config \  
&& su taiga -c "cd ~ \  
&& git clone https://github.com/taigaio/taiga-back.git taiga-back \  
&& cd taiga-back \  
&& git checkout stable \  
&& sudo pip install -r requirements.txt \  
&& python manage.py compilemessages \  
&& python manage.py collectstatic --noinput"  
  
COPY docker-entrypoint.sh /  
  
USER taiga  
  
WORKDIR /home/taiga/taiga-back  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8000  
  
CMD ["taiga"]  

