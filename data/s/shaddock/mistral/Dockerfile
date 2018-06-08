FROM shaddock/seed:juno  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
# Install Mistral  
RUN \  
apt-get update &&\  
apt-get install -y python-dev python-setuptools libffi-dev libxslt1-dev\  
libxml2-dev libyaml-dev libssl-dev git  
  
RUN \  
git clone https://github.com/stackforge/mistral.git &&\  
cd mistral && python setup.py install &&\  
pip install pbr &&\  
pip install -e .  
  
ADD supervisord.conf /etc/supervisord.conf  
  
ADD mistral-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN chmod +x /usr/local/bin/mistral-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
#EXPOSE 8082  
CMD ["mistral-start"]  

