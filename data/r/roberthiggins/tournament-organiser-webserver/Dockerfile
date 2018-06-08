# This will fire up the webserver.  
FROM django:python2  
MAINTAINER Robert Higgins <robert.h.higgins@gmail.com>  
  
# Set up Django  
ADD ./requirements.txt ./requirements.txt  
RUN pip install -r requirements.txt  
  
RUN apt-get update && apt-get install -y curl  
  
# Content  
# The original src of the src/ dir used here can be found on github  
# https://github.com/roberthiggins/Tournament_Organizer-  
# in the webserver directory.  
ADD src/ webapp/  
ADD ./init.sh webapp/  
ADD ./bash_aliases /root/.bash_aliases  
  
# Config  
WORKDIR webapp/  
  
CMD bash ./init.sh && python manage.py runserver 0.0.0.0:8000  

