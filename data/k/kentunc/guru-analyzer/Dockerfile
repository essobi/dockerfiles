FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
git \  
postgresql \  
python3-dev \  
python3-pip  
  
USER postgres  
  
RUN /etc/init.d/postgresql start \  
&& psql --command "CREATE USER root WITH SUPERUSER PASSWORD 'root';" \  
&& createdb -O root cas  
  
USER root  
  
WORKDIR /root  
  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add - \  
&& echo "deb http://cran.ma.imperial.ac.uk/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y r-base \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config.json /root/  
  
RUN /etc/init.d/postgresql start \  
&& pip3 install \  
rpy2 \  
sqlalchemy \  
py-postgresql \  
requests \  
python-dateutil \  
http://pypi.python.org/packages/source/M/MonthDelta/MonthDelta-1.0b.tar.bz2 \  
&& git clone
https://github.com/CommitAnalyzingService/CAS_CodeRepoAnalyzer.git \  
&& python3 ./CAS_CodeRepoAnalyzer/script.py initDb  
  
CMD ["python3", "/data/CAS_CodeRepoAnalyzer/script.py"]  

