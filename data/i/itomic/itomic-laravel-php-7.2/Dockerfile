FROM ubuntu:16.04  
MAINTAINER Itomic Tech <tech@itomic.com.au>  
  
# Install dependencies.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python-software-properties \  
software-properties-common \  
rsyslog systemd systemd-cron sudo \  
curl wget less gettext \  
zip unzip bzip2 tar \  
ruby python python3 perl \  
memcached libzip-dev libmcrypt-dev \  
apt-transport-https automake autoconf \  
&& rm -Rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
RUN sed -i 's/^\\($ModLoad imklog\\)/#\1/' /etc/rsyslog.conf  
#ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
# Install The Chrome Web Driver & Dusk Utilities  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libxpm4 libxrender1 libgtk2.0-0 \  
libnss3 libgconf-2-4 chromium-browser \  
xvfb gtk2-engines-pixbuf xfonts-cyrillic \  
xfonts-100dpi xfonts-75dpi xfonts-base \  
xfonts-scalable imagemagick x11-apps  
  
# Install Ansible  
RUN add-apt-repository -y ppa:ansible/ansible \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ansible \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
COPY initctl_faker .  
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker
/sbin/initctl  
  
# Install Ansible inventory file  
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts  
  
# Copy provisioning directory, variable overrides, and scripts into container.  
COPY ./ /etc/ansible/laravel-vm  
COPY ./provisioning/docker/vars/docker-hub-overrides.yml /etc/ansible/laravel-
vm/local.config.yml  
  
# Provision Drupal VM inside Docker.  
RUN ansible-playbook /etc/ansible/laravel-vm/provisioning/playbook.yml  
  
CMD ["/lib/systemd/systemd"]  
  
# Add mysql  
#ENV DEBIAN_FRONTEND=noninteractive  
#RUN echo "mysql-server mysql-server/root_password password " | debconf-set-
selections  
#RUN echo "mysql-server mysql-server/root_password_again password " | debconf-
set-selections  
#RUN apt-get -y install mysql-server mysql-client libmysqlclient-dev  
#RUN mysql_secure_installation  

