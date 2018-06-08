FROM python:3.4  
  
MAINTAINER Byron Ruth <b@devel.io>  
  
# Install dependencies  
RUN apt-get -qq update  
RUN apt-get -qq install -y git  
RUN apt-get -qq install -y postgresql  
  
# Generator dependencies  
RUN pip -q install SQLAlchemy==0.9.8  
RUN pip -q install PyMySQL==0.6.3  
RUN pip -q install PyVCF==0.6.7  
RUN pip -q install SQLAlchemy==0.9.8  
RUN pip -q install openpyxl==2.1.4  
RUN pip -q install psycopg2==2.5.4  
RUN pip -q install pymongo==2.7.2  
  
# Not yet available on PyPi  
RUN pip -q install "https://github.com/chop-dbhi/origins-generator-
service/tarball/master#egg=origins-generator-service"  
  
EXPOSE 5000  
  
ENTRYPOINT ["origins-generators", "--host", "0.0.0.0"]  

