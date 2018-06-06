FROM logstash:2.4  
MAINTAINER Joost van der Griendt <joostvdg@gmail.com>  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL version="1.0.0"  
LABEL description="Docker container for configuring LogStash for Flusso
Drove'"  
COPY config/logstash.conf /conf/  
CMD ["-f", "/conf/logstash.conf"]

