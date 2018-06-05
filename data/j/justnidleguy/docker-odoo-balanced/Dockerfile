FROM justnidleguy/docker-odoo:v1.0  
MAINTAINER Mauro Usuga <justnidleguy@gmail.com>  
  
RUN apt-get install unzip  
RUN pip install boto redis  
RUN wget -q -O /tmp/s3_attachment.zip
https://github.com/justnidleguy/odoo-s3-attachment/archive/v1.0.zip && unzip
/tmp/s3_attachment.zip -d /opt/odoo/addons && rm /tmp/s3_attachment.zip  
  
# apply patches..., etc  

