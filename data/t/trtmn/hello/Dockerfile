FROM ubuntu:16.04  
MAINTAINER = matt@thetroutmans.net  
EXPOSE 80  
RUN apt-get update && apt-get install -y python3 python3-pip nginx git nano
sqlite3  
ADD ./ /hello  
RUN pip3 install -r /hello/trtmn/config_files/requirements.txt  
RUN cp /hello/trtmn/config_files/gunicorn.conf /etc/init/gunicorn.conf  
RUN cp /hello/trtmn/config_files/nginx /etc/nginx/sites-available/trtmn  
WORKDIR /hello/trtmn  
RUN python3 manage.py makemigrations  
RUN python3 manage.py migrate  
RUN echo "from django.contrib.auth.models import User;
User.objects.create_superuser('admin', 'admin@example.com', 'admin')" |
python3 manage.py shell  
RUN sqlite3 db.sqlite3 "INSERT INTO hello_contactinfo
VALUES(1,'default','2016-06-17 20:15:50','Matt','Troutman','Quality Assurance
Engineer','Hi. Call me
Fishy','m@trtmn.com','2025-01-01','4159934749','2025-01-01','trtmn','m.trtmn','trtmn','trtmn','Matt
Troutman is a Quality Assurance Engineer that has been in the tech industry
for over 10 years.','Python, Django, Docker, nginx, gunicorn, git',1);"  
RUN python3 manage.py collectstatic --noinput  
RUN ln -s /etc/nginx/sites-available/trtmn /etc/nginx/sites-enabled  
RUN touch /var/log/nginx/access.log  
RUN rm /etc/nginx/sites-available/default  
CMD /hello/trtmn/config_files/startup.sh

