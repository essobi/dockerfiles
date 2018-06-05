FROM ampersandtarski/ampersand-prototype:texlive  
# build RAP3 application by cloning the models repository  
RUN mkdir -p ~/git \  
&& cd ~/git \  
&& git clone \--depth=1 \--branch master
https://github.com/AmpersandTarski/RAP \  
# build RAP3 application  
&& ampersand ~/git/RAP/RAP3/RAP3prod.adl \--config=RAP/RAP3/RAP3prod.yaml
-p/var/www/html/RAP3 \  
&& mkdir -p /var/www/html/RAP3/log \  
&& chown -R www-data:www-data /var/www/html/RAP3  
  
VOLUME /var/www/html/RAP3  
# build Enrollment demo, which is being used in the Ampersand-tutorial  
RUN ampersand -p/var/www/html/Enroll ~/git/RAP/Demos/Enroll/Enrollment.adl
\--verbose \  
&& chown -R www-data:www-data /var/www/html/Enroll  

