FROM ruby:2.2.2  
RUN curl -sSL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y nodejs \  
&& apt-get -qy autoremove \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN cd /opt \  
&& git clone https://github.com/ConradIrwin/showterm.io \  
&& cd /opt/showterm.io \  
&& bundle install  
  
WORKDIR /opt/showterm.io  
  
COPY resources/database.yml config/  
COPY resources/init.sh /init.sh  
  
VOLUME /data  
EXPOSE 3000  
CMD ["/init.sh"]  

