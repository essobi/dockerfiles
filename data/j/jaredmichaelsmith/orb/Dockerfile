FROM python:3-onbuild  
MAINTAINER Foreseer Framework <foreseer@utk.edu>  
  
WORKDIR /home/orb  
  
ENV ORB_SETTINGS "orb.settings.ProdConfig"  
ENV DATABASE_URL "mysql+pymysql://jms:jms@da0.eecs.utk.edu/orb"  
EXPOSE 9020  
ADD src /home/orb/src/  
  
RUN cd /home/orb/src && python manage.py db init && python manage.py db
migrate \  
&& python manage.py db upgrade && run.sh  
  
# ENTRYPOINT ["python", "manage.py"]  

