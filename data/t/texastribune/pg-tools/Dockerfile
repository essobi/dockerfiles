FROM texastribune/base  
MAINTAINER tech@texastribune.org  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
ENV PG_MAJOR 9.4  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && apt-get install -y \  
curl \  
postgresql-client-$PG_MAJOR \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN pip install awscli postdoc  
  
ADD . /app  
  
ENTRYPOINT ["/bin/bash"]  

