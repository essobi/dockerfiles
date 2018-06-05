FROM sumitchawla/vertica  
MAINTAINER Talles Bertann "talles.bertann@gmail.com"  
ENV SHELL "/bin/bash"  
ENV TERM dumb  
  
USER dbadmin  
RUN /opt/vertica/bin/admintools -t create_db -s localhost -d dw -p a4pmdw -c
/home/dbadmin/dw/catalog -D /home/dbadmin/dw/data  
  
USER root  
ENV VERTICADATA /home/dbadmin/dw  
VOLUME /home/dbadmin/dw  
  
RUN cd home \  
&& wget -O vertdump.zip
https://github.com/gleisonsilva/vertdump/archive/master.zip \  
&& apt-get update \  
&& apt-get install zip unzip \  
&& unzip vertdump.zip \  
&& rm vertdump.zip  
  
ADD assets /assets  
  
RUN cd assets \  
&& chmod 777 docker-entrypoint.sh  
  
ENTRYPOINT ["assets/docker-entrypoint.sh"]

