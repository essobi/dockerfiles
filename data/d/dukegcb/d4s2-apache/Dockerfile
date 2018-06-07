FROM dukegcb/d4s2  
MAINTAINER dan.leehr@duke.edu  
  
# apache2 / supervisor  
RUN apt-get update \  
&& apt-get install -y apache2 libapache2-mod-wsgi vim\  
&& apt-get clean  
RUN pip install supervisor  
  
# Configure supervisor  
ADD supervisord.conf /etc/supervisord.conf  
  
# Configure Apache  
ADD d4s2.conf /etc/apache2/sites-available/d4s2.conf  
RUN a2enmod ssl  
RUN a2ensite d4s2  
  
# Ensure services are stopped so that supervisor can run them  
RUN service apache2 stop  
  
# Additional requirements for production instance  
ADD start-apache.sh /usr/src/app/  
  
# Replace settings with production-specific  
COPY settings.docker-production /usr/src/app/d4s2/settings.py  
  
# Place static files using manage.py  
# Running any manage.py commands require a secret key to be present  
# in the django app's settings.py.  
ENV D4S2_SECRET_KEY=secret  
RUN python manage.py collectstatic --noinput  
# Reset the variable to an empty string, requiring it to be provided at
runtime  
ENV D4S2_SERVICE_SECRET_KEY=''  
# Volume for certificates  
VOLUME /etc/external/  
  
EXPOSE 80  
EXPOSE 443  
CMD supervisord -c /etc/supervisord.conf -n  
  

