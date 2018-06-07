FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update \  
&& apt-get install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& /usr/bin/ssh-keygen -A  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
git \  
build-essential \  
linux-headers-amd64 \  
postgresql-client \  
postgresql-contrib \  
libpq-dev \  
;  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN pip install virtualenv  
  
RUN virtualenv /home/django/venv  
RUN . /home/django/venv/bin/activate  
  
WORKDIR /opt/django  
ADD requirements.txt /opt/django  
RUN pip install -r requirements.txt  
  
RUN echo 'db:5432:*:django:django' > ~/.pgpass; \  
chmod 600 ~/.pgpass;  
  
ADD . /opt/django  
  
EXPOSE 22 8000  
ENV CQLENG_ALLOW_SCHEMA_MANAGEMENT="True"  
CMD ["source /home/django/bin/activate"]  

