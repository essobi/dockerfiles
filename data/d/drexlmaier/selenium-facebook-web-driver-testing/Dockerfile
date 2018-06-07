FROM selenium/standalone-chrome-debug  
LABEL Description="selenium-facebook-web-driver-testing"
Vendor="SPURENELEMENTE GmbH" Version="1.4" maintainer="daniel@se-medien.de"  
MAINTAINER daniel@se-medien.de  
  
  
USER root  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y unzip wget sudo bzip2 gnupg apt-utils curl apt-
transport-https ca-certificates \  
&& apt-get clean  
#&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get update \  
&& apt-get install -y php-cli php-dev php-curl php-xml php-zip php-mbstring  
  
# Install Composer  
RUN cd /usr/local/bin \  
&& curl -sS https://getcomposer.org/installer | php \  
&& php composer.phar require facebook/webdriver  
  
RUN echo 'root:secret' | chpasswd  
  
ADD example.php /usr/local/bin  
  
# Run Chrome non-privileged  
#USER chrome  
# Expose port 9222  
EXPOSE 9222  
EXPOSE 4444  
# Autorun chrome headless with no GPU  
#ENTRYPOINT [ "google-chrome-stable" ]  
#CMD [ "--headless", "--disable-gpu", "--remote-debugging-address=0.0.0.0", "
--remote-debugging-port=9222" ]  
#RUN cd /usr/local/bin && php example.php  

