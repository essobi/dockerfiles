FROM ruby:2.2.2  
# Groonga(http://groonga.org/docs/install/debian.html)  
RUN echo "deb http://packages.groonga.org/debian/ jessie main" >>
/etc/apt/sources.list.d/groonga.list \  
&& echo "deb-src http://packages.groonga.org/debian/ jessie main" >>
/etc/apt/sources.list.d/groonga.list \  
&& apt-get update \  
&& apt-get install -y --allow-unauthenticated groonga-keyring \  
&& apt-get update \  
&& apt-get install -y libgroonga-dev  
  
# Milkode  
RUN gem install milkode --no-ri --no-rdoc  
RUN milk init --default  
  
# Add packages  
ONBUILD ADD . /home/  
ONBUILD RUN (cd /home && milk add --from-file=packages)  
  
# Run  
EXPOSE 9292  
CMD milk web --host=0.0.0.0 --no-browser  

