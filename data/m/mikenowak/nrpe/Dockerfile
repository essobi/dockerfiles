FROM alpine:edge  
  
RUN apk add --no-cache perl ruby ruby-json nrpe nagios-plugins-procs nagios-
plugins-time nagios-plugins-load nagios-plugins-swap nagios-plugins-disk
python3  
  
ADD check_memory check_time_skew check_oxidized.rb check_docker
/usr/lib/nagios/plugins/  
ADD nrpe.cfg /etc/nrpe.cfg  
ADD entrypoint.sh /entrypoint.sh  
  
EXPOSE 5666  
CMD /entrypoint.sh  

