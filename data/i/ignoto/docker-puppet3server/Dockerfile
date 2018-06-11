FROM debian  
MAINTAINER Antonio Xanxess <dr.ignoto@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV FQDN testpuppet.example  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN apt-get update  
  
RUN echo "locales locales/locales_to_be_generated multiselect es_ES.UTF-8
UTF-8" | debconf-set-selections &&\  
echo "locales locales/default_environment_locale select es_ES.UTF-8" |
debconf-set-selections  
  
RUN apt-get install -y locales wget  
  
ENV LC_ALL es_ES.UTF-8  
RUN wget http://apt.puppetlabs.com/puppetlabs-release-jessie.deb && dpkg -i
puppetlabs-release-jessie.deb && apt-get update && apt-get install -y \  
puppet \  
puppetmaster-passenger \  
subversion \  
&& apt-get clean  
  
COPY puppetmaster.conf /etc/apache2/sites-available/  
  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8140  
CMD ["-D", "FOREGROUND"]  

