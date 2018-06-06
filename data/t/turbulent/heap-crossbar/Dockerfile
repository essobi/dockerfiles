FROM turbulent/heap-base:3.0.0  
MAINTAINER Philippe Milot <pmilot@turbulent.ca>  
  
ENV heap-crossbar 1.0.1  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install \  
build-essential \  
libssl-dev \  
libffi-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install -U pip  
RUN pip install crossbar  
  
# Make sure crossbar is installed  
RUN crossbar version  
  
COPY supervisor.conf.tmpl /systpl/  
  
ADD run.sh /  
ADD run-crossbar.sh /  
  
VOLUME ["/vol/logs"]  
VOLUME ["/vol/spool"]  
VOLUME ["/vol/website"]  
  
EXPOSE 8080  
EXPOSE 8000  
CMD ["/run.sh"]  

