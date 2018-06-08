FROM michaelsauter/alpine:3.3  
MAINTAINER Michael Sauter <mail@michaelsauter.net>  
  
RUN sudo apk-install postgresql=9.4.5-r1  
  
ADD postgres /postgres  
RUN sudo chown postgres: /postgres  
  
ADD bin/start-postgres /usr/local/bin/start-postgres  
RUN sudo chmod 0755 /usr/local/bin/start-postgres  
  
WORKDIR /postgres  
ENV HOME /home/postgres  
USER postgres  
EXPOSE 5432  
CMD ["start-postgres"]  

