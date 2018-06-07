FROM ubuntu:trusty  
  
MAINTAINER Karol Kozakowski <karol.kozakowski@coi.gov.pl>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HERALD_USER herald  
ENV HERALD_USER_ID 442  
ENV HERALD_HOMEDIR /home/$HERALD_USER  
ENV HERALD_VERSION '0.8.1'  
RUN apt-get update  
RUN apt-get install -y ruby libpq-dev ruby-dev make gcc g++ postgresql-client  
RUN gem install puppet-herald --version $HERALD_VERSION  
RUN gem install pg puma  
RUN gem install therubyracer  
  
RUN useradd --system --create-home --uid $HERALD_USER_ID \--home-dir
$HERALD_HOMEDIR $HERALD_USER  
RUN mkdir /etc/pherald  
RUN touch /etc/pherald/passfile  
RUN chown $HERALD_USER:$HERALD_USER /etc/pherald/passfile  
RUN chmod 0600 /etc/pherald/passfile  
  
COPY src/herald_start.sh /usr/local/sbin/herald-start  
RUN chmod +x /usr/local/sbin/herald-start  
  
USER $HERALD_USER  
# TODO: Remove this when GH:wavesoftware/gem-puppet-herald#25 gets resolved  
WORKDIR /var/lib/gems/1.9.1/gems/puppet-herald-$HERALD_VERSION  
CMD ["/usr/local/sbin/herald-start"]  

