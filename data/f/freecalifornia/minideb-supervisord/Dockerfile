FROM bitnami/minideb:stretch  
  
# Enable https download of packages  
RUN apt update -yqq \  
&& apt upgrade -yqq \  
&& install_packages apt-transport-https ca-certificates \  
&& update-ca-certificates  
  
# Basic Dependencies  
RUN install_packages \  
curl \  
#sudo git \  
# manage all processes in the container, act as  
# init script, has PID 1 and handles POSIX signals  
supervisor \  
python-setuptools \  
# for automated security updates  
unattended-upgrades \  
# install the tool to rotate logs  
logrotate \  
# Adds envsubst command which inject env vars into files  
gettext \  
# reliable syslog  
rsyslog \  
&& service rsyslog start  
  
# configuring supervisor  
COPY config/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
COPY config/supervisor/cron.conf /etc/supervisor/conf.d/cron.conf  
RUN /usr/bin/easy_install supervisor-stdout \  
&& mkdir -p /var/log/supervisor \  
&& mkdir -p /var/run/supervisor \  
&& chmod 700 /etc/supervisor/supervisord.conf  
  
# configuring logrotate to run as cron job  
COPY config/cron/logrotate /etc/cron.d/logrotate  
  
# configuring logrotate on supervisor log files  
COPY config/logrotate/supervisord /etc/logrotate.d/supervisord  
  
# apt upgrade configuration  
COPY config/02periodic /etc/apt/apt.conf.d/02periodic  
  
# Fix debian cron bug https://stackoverflow.com/a/38850273  
RUN touch /etc/crontab /etc/cron.*/* && chown root:root -R /etc/cron.d/  
  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/supervisord.conf"]  

