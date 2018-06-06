  
FROM finalcut/coldfusion10  
MAINTAINER fridus detry.florent@gmail.com  
  
# jvm config  
ADD ./build/jvm.config /opt/coldfusion10/cfusion/bin/jvm.config  
RUN chmod 777 /opt/coldfusion10/cfusion/bin/jvm.config  
  
# service  
RUN mv /opt/coldfusion10/cfusion/bin/coldfusion
/opt/coldfusion10/cfusion/bin/coldfusion_bk  
ADD ./build/coldfusion-service /opt/coldfusion10/cfusion/bin/coldfusion  
RUN chmod +x /opt/coldfusion10/cfusion/bin/coldfusion && ln -s
/opt/coldfusion10/cfusion/bin/coldfusion /etc/init.d/coldfusion  
  
# gateway  
ADD ./build/cfapi-json-gateway/Gateway.cfc /CF/Gateway.cfc  
COPY ./build/vhost-default /etc/apache2/sites-available/default  
  
# apache modules  
RUN a2enmod rewrite && a2enmod headers  
  
# wkhtmltopdf  
RUN apt-get -qq update && apt-get install -y curl php5 php5-gd  
ADD ./build/install_wkhtmltopdf.sh /tmp/install_wkhtmltopdf.sh  
RUN /tmp/install_wkhtmltopdf.sh  
  
# Timezone  
RUN echo Europe/Brussels | sudo tee /etc/timezone && sudo dpkg-reconfigure
--frontend noninteractive tzdata  
  
# jq  
RUN wget --quiet https://github.com/stedolan/jq/releases/download/jq-1.5/jq-
linux64 && \  
chmod +x jq-linux64 && \  
mv jq-linux64 /usr/bin/jq  
  
ADD ./build/start.sh /start.sh  
CMD /start.sh  

