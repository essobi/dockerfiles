FROM ubuntu:16.04  
RUN apt-get update && apt-get -y install python3 python3-dev \  
python3-setuptools build-essential libxml2-dev libxslt1-dev libffi-dev \  
graphviz libpq-dev libssl-dev zlib1g-dev ca-certificates \  
postgresql postgresql-client sudo \  
wget vim nano joe htop net-tools iputils-ping traceroute socat mtr host iperf3
curl iproute2 tcpdump telnet  
RUN easy_install3 pip  
  
RUN wget https://github.com/digitalocean/netbox/archive/v2.3.3.tar.gz && tar
xzf v2.3.3.tar.gz -C /opt  
  
RUN ln -s /opt/netbox-2.3.3 /opt/netbox  
RUN cd /opt/netbox-2.3.3 && pip3 install -r requirements.txt  
  
RUN pip3 install napalm  
  
RUN cp /opt/netbox/netbox/netbox/configuration.example.py
/opt/netbox/netbox/netbox/configuration.py  
RUN sed -i.bak "s/ALLOWED_HOSTS = \\[\\]/ALLOWED_HOSTS = \\['*'\\]/g"
/opt/netbox/netbox/netbox/configuration.py  
RUN sed -i.bak "s/'USER': '',/'USER': 'postgres',/g"
/opt/netbox/netbox/netbox/configuration.py  
RUN sed -i.bak "s/'PASSWORD': '',/'PASSWORD': 'nmm-secret',/g"
/opt/netbox/netbox/netbox/configuration.py  
RUN sed -i.bak "s/SECRET_KEY = ''/SECRET_KEY = 'this-is-not-in-anyway-
secure_just-for-demo-purposes'/g" /opt/netbox/netbox/netbox/configuration.py  
  
RUN service postgresql start && sudo -u postgres psql -U postgres -d postgres
-c "alter user postgres with password 'nmm-secret';" && \  
sudo -u postgres createdb -O postgres netbox && \  
python3 /opt/netbox/netbox/manage.py migrate && \  
python3 /opt/netbox/netbox/manage.py shell -c "from django.contrib.auth.models
import User; User.objects.create_superuser('admin', 'admin@example.com', 'nmm-
secret')" && \  
python3 /opt/netbox/netbox/manage.py collectstatic --no-input  
  
ADD start-services.sh /root/start-services.sh  
RUN chmod +x /root/start-services.sh  
  
CMD /root/start-services.sh  
  
VOLUME /root /var/lib/postgresql  

