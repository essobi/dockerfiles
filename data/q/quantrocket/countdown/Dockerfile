FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
RUN apt-get update && apt-get install -y \  
cron \  
supervisor \  
&& /bin/bash -c "source activate /opt/conda" \  
&& pip install -U quantrocket-client \  
&& /bin/bash -c "source deactivate"  
  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY crontab_demo /tmp/  
COPY uwsgi /etc/uwsgi  
  
# Install curl wrapper -- Bitbucket issue #2  
COPY curl /opt/countdown/bin/curl  
RUN touch /opt/countdown/__init__.py \  
&& chmod +x /opt/countdown/bin/* \  
# crontab PATH=/usr/bin:/bin, so symlink /usr/bin/curl to the wrapper  
&& ln -sf /opt/countdown/bin/curl /usr/bin/curl \  
# non-crontab PATH=/opt/conda/bin:/usr/local/sbin:... etc, so put our  
# wrapper first in case running curl outside of crontab  
&& echo "/opt/countdown" > /opt/conda/lib/python3.6/site-
packages/countdown.pth  
ENV PATH="/opt/countdown/bin:$PATH"  
# Add quantrocket_wrapper to cron path (crontab PATH=/usr/bin:/bin)  
COPY quantrocket_wrapper /usr/bin/quantrocket  
RUN chmod +x /usr/bin/quantrocket  
  
COPY qrocket /tmp/uwsgi/qrocket  
  
# Build uwsgi  
RUN /tmp/build.sh  
  
CMD ["/usr/bin/supervisord"]  

