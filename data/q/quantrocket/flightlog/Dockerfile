FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
RUN /bin/bash -c "source activate /opt/conda" \  
&& pip install termcolor==1.1.0 \  
&& pip install twilio==6.1.0 \  
&& /bin/bash -c "source deactivate"  
  
COPY uwsgi /etc/uwsgi/  
COPY qrocket /tmp/uwsgi/qrocket  
  
RUN /tmp/build.sh  
  
EXPOSE 9020  
CMD ["uwsgi-quantrocket", "--emperor", "/etc/uwsgi/uwsgi*.ini"]  

