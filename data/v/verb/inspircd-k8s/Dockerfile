FROM debian:8  
MAINTAINER Lee Verberne <lee@blarg.org>  
  
RUN apt-get update && apt-get install -y \  
inspircd \  
&& rm -rf /var/lib/apt/lists/*  
RUN mkdir -p /usr/lib/inspircd/logs && chown irc /usr/lib/inspircd/logs  
  
USER irc  
CMD ["/usr/sbin/inspircd", "--nofork"]  

