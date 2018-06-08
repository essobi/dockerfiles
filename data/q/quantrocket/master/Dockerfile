FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
RUN /bin/bash -c "source activate /opt/conda" \  
&& pip install bdateutil==0.1 \  
&& /bin/bash -c "source deactivate"  
  
ENV IBG_CLIENT_RANGE=2000 UWSGI_WORKERS=3  
COPY qrocket /tmp/uwsgi/qrocket  
COPY uwsgi /etc/uwsgi  
COPY quantrocket.master.main.schema.sql /var/opt/  
COPY timezones.csv /tmp/timezones.csv  
  
RUN mkdir -p /codeload \  
&& mkdir -p /var/lib/quantrocket \  
&& mkdir -p /tmp/universes \  
&& mkdir -p /tmp/ticksize \  
&& mkdir -p /tmp/diffs \  
&& mkdir -p /tmp/options \  
&& mkdir -p /tmp/securities \  
&& mkdir -p /var/tmp/uwsgi/mule/kwargs/diffs \  
&& mkdir -p /var/tmp/uwsgi/mule/kwargs/listings \  
&& mkdir -p /var/tmp/uwsgi/mule/kwargs/options \  
&& /tmp/build.sh  

