FROM michaelpc/perl-base:latest  
  
VOLUME /web/repo  
VOLUME /root/.cpanm  
VOLUME /var/log/pinto  
  
ENV PROJECT_NAME "Local CPAN Repository"  
ENV PINTO_REPOSITORY_ROOT /web/repo  
  
RUN apt-get update; apt-get install -y apache2-utils  
  
COPY . /web  
  
WORKDIR /web  
  
RUN ln -vs /web/bin/start-pinto.sh /etc/init.d/pinto-server  
  
RUN cpanm --notest Pinto Pinto::Action::Doc Authen::Simple::Passwd
Capture::Tiny  
  
EXPOSE 8080  
ENV INITD_START_PINTO pinto-server  

