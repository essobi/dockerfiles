# Dockerfile  
# https://github.com/pommi/mendix-docker/blob/master/Dockerfile  
# VERSION 0.1  
FROM mendix/wheezy  
MAINTAINER Pim van den Berg <pim.van.den.berg@mendix.com>  
  
RUN useradd -m mendix  
  
ADD sources.list /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get -o Apt::Get::AllowUnauthenticated=yes install -y debian-mendix-
keyring  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends python-m2ee oracle-j2re1.6
nginx python-flask postgresql-client  
RUN apt-get clean  
  
RUN cd /home/mendix; mkdir -p .m2ee runtimes log data data/files data/model-
upload data/database model web tmp  
  
ADD m2ee.yaml /home/mendix/.m2ee/m2ee.yaml  
ADD nginx.conf /home/mendix/nginx.conf  
  
RUN chown -R mendix:mendix /home/mendix /var/log/nginx /var/lib/nginx  
  
RUN wget -q https://raw.github.com/pommi/m2ee-tools/docker/src/m2ee-api.py -O
/usr/bin/m2ee-api  
RUN chmod +x /usr/bin/m2ee-api  
  
EXPOSE 5000 7000  
CMD ["/bin/su", "mendix", "-c", "/usr/bin/m2ee-api"]

