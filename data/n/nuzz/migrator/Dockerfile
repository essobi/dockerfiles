FROM python:2.7.14-jessie  
MAINTAINER Matt Nuzzaco <nuzz@sightmachine.com>  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.6 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.6.list  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libssl-dev\  
mongodb-org-tools  
ADD https://storage.googleapis.com/pub/gsutil.tar.gz /  
RUN tar xfz gsutil.tar.gz  
ENV PATH=${PATH}:/gsutil  
# for testing only  
CMD ["sh", "-c", "tail -f /dev/null"]  

