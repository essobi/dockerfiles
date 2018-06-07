FROM ubuntu:14.04  
MAINTAINER James Lee Vann  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y build-
essential python3 python3-dev python3-pip git  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libjpeg-dev libpng-dev
libpqxx3-dev \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/*  
RUN pip3 install virtualenv  
RUN pip3 install uwsgi  
RUN pip3 install vex  
  
VOLUME ["/data", "/code"]  
  
ADD run.sh /run.sh  
RUN ["chmod", "+x", "run.sh"]  
  
EXPOSE 5000  
CMD ["/run.sh"]  
  

