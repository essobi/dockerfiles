FROM python:3.5  
ARG BUILD_USER=django  
ARG BUILD_USER_GROUP=django  
ARG BUILD_USER_PASSWORD=django  
ARG BUILD_USER_SHELL=/bin/bash  
ARG BUILD_USER_UID=1000  
ARG BUILD_USER_GID=1000  
ARG BUILD_USER_HOME=/home/django  
ARG BUILD_PROJECT_PATH=/opt/django  
ARG BUILD_PROJECT_PORT=8000  
ENV PYTHONUNBUFFERED 1  
ENV DJANGO_USER=${BUILD_USER}  
ENV DJANGO_USER_GROUP=${BUILD_USER_GROUP}  
ENV DJANGO_USER_PASSWORD=${BUILD_USER_PASSWORD}  
ENV DJANGO_USER_SHELL=${BUILD_USER_SHELL}  
ENV DJANGO_USER_UID=${BUILD_USER_UID}  
ENV DJANGO_USER_HOME=${BUILD_USER_HOME}  
ENV PROJECT_PATH=${BUILD_PROJECT_PATH}  
ENV PROJECT_PORT=${BUILD_PROJECT_PORT}  
ENV VENV_PATH=${DJANGO_USER_HOME}/venv/  
ENV VENV_PIP=${VENV_PATH}/bin/pip3  
ENV VENV_PY=${VENV_PATH}/bin/python  
  
  
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
  
WORKDIR ${PROJECT_PATH}  
  
ADD requirements.txt ${PROJECT_PATH}  
  
RUN virtualenv -p $(which python3) ${VENV_PATH}  
#RUN ${VENV_PATH}/bin/pip install -r requirements.txt  
RUN echo 'db:5432:*:django:django' > ~/.pgpass; \  
chmod 600 ~/.pgpass;  
  
ADD . ${PROJECT_PATH}  
  
ENV CQLENG_ALLOW_SCHEMA_MANAGEMENT="True"  
USER root  
  
RUN apt-get update \  
&& apt-get install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& echo "root:root" | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& /usr/bin/ssh-keygen -A  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Cleaning installation files  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 22  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]

