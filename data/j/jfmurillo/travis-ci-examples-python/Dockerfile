FROM ubuntu:trusty  
  
#RUN echo "deb http://ppa.launchpad.net/pypy/ppa/ubuntu trusty main" > \  
# /etc/apt/sources.list.d/pypy-ppa.list  
#RUN apt-key adv --keyserver keyserver.ubuntu.com \  
# --recv-keys 2862D0785AFACD8C65B23DB0251104D968854915  
#RUN apt-get update  
# Add the application resources URL  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main
universe" >> /etc/apt/sources.list  
  
# Update the sources list  
RUN apt-get update  
  
RUN apt-get install -qyy \  
-o APT::Install-Recommends=false -o APT::Install-Suggests=false \  
python-pip python-dev python-psycopg2 build-essential python-virtualenv pypy
libffi6 python-psycopg2  
  
RUN virtualenv -p /usr/bin/pypy /appenv  
RUN . /appenv/bin/activate  
RUN pip install flask  
ADD . /code  
WORKDIR /code  
  
# Expose ports  
EXPOSE 8080  
CMD python app.py

