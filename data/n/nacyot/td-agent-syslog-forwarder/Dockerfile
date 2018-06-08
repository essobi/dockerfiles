FROM nacyot/td-agent:latest  
MAINTAINER Daekwon Kim <propellerheaven@gmail.com>  
  
ENV SYSLOG_TYPE syslog  
ENV SYSLOG_TAG syslog.udp  
ENV SYSLOG_TIME_FORMAT time_format %Y-%m-%dT%H:%M:%SZ  
ENV SYSLOG_FORMAT ^(?:[0-9]+)? (?<time>.*?) (?<host_name>.*?)
(?<container_name>.*?) (?<pid>[0-9]+) - - (?<event>.*?)$  
ENV SYSLOG_BIND 0.0.0.0  
ENV SYSLOG_PORT 5140  
ENV FORWARD_HOST 127.0.0.1  
ENV FORWARD_PORT 5140  
ENV FLUSH_INTERVAL 10s  
  
WORKDIR /root  
ADD ./config/td-agent.conf /etc/td-agent/td-agent.conf  
ADD ./setup_configs.sh /root/setup_configs.sh  
ADD ./run.sh /root/run.sh  
  
VOLUME /log-data  
RUN chmod +x /root/run.sh /root/setup_configs.sh  
EXPOSE 24224 5140/udp  
  
CMD ./setup_configs.sh && ./run.sh  

