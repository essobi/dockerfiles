FROM turbulent/heap-app:4.0.0  
MAINTAINER Philippe Milot <b@turbulent.ca>  
  
ENV heap-daemon 1.0.0  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install pkg-config php7.1-dev libevent-dev && \  
pecl install event && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ADD supervisor.conf.tmpl /systpl/  
  
ADD run-program.sh /  
ADD run-watcher.sh /  
  
ADD event.ini /etc/php/7.1/mods-available/  
RUN ln -sf /etc/php/7.1/mods-available/event.ini
/etc/php/7.1/cli/conf.d/21-event.ini  
  
COPY run.sh /  
  
ENV VAR_COMMAND="unset-program.php" \  
VAR_WATCH=""  

