# vim:set ft=dockerfile:  
FROM debian:testing  
MAINTAINER Gregor Jerše <gregor.jerse@fri.uni-lj.si>  
  
ENV URNIK_GIT_LOCATION=https://github.com/ul-fri/urnik.git  
ENV URNIK_GIT_BRANCH=master  
  
# Secret key is only here to make collectstatic work.  
# It is overrided from settings in docker-compose.  
ENV SECRET_KEY=very_secret_key  
  
# Add Tomo user and group first to make sure their IDs get assigned
consistently  
RUN groupadd -r timetable && useradd -r -g timetable timetable  
  
# Change locale to en_US.UTF-8  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install required packages  
RUN apt-get update \  
&& apt-get install -y \  
uwsgi \  
uwsgi-plugin-python3 \  
python3 \  
python3-pip \  
git \  
postgresql-server-dev-all \  
libpython3-dev \  
libsasl2-dev \  
libldap2-dev \  
unixodbc-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /home/timetable  
  
# Pull tomo source into current working directory  
RUN git clone -b ${URNIK_GIT_BRANCH} ${URNIK_GIT_LOCATION}  
  
# Install dependencies  
RUN pip3 install -r urnik/requirements_development.txt  
RUN pip3 install --upgrade --force-reinstall pyldap  
  
RUN python3 urnik/manage.py collectstatic --noinput
--settings=urnik_fri.settings_example  
RUN chown timetable.timetable -R /home/timetable  
  
# UWSGI options are read from environmental variables.  
# They are specified in docker-compose file.  
CMD ["uwsgi"]  

