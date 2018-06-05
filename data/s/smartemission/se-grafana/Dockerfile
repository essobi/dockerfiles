FROM grafana/grafana:5.1.3  
LABEL maintainer="Just van den Broecke <justb4@gmail.com>"  
  
ENV TZ Europe/Amsterdam  
USER root  
  
# Needed for 'envsubst' util.  
RUN \  
apt-get update \  
&& apt-get -y install gettext-base \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY provisioning /var/smartem/templates  
COPY provisioning /var/smartem/provisioning  
  
COPY entry.sh /entry.sh  
RUN chmod +x /entry.sh  
ENTRYPOINT [ "/entry.sh" ]  

