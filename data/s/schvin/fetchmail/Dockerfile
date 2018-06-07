FROM ubuntu:trusty  
MAINTAINER George Lewis <schvin@schvin.net>  
  
ENV REFRESHED_AT 2014-11-18  
RUN apt-get update --fix-missing -y && apt-get upgrade -y  
RUN apt-get install -y fetchmail  
  
RUN groupadd s-mail  
RUN useradd s-mail -g s-mail -d /home/s-mail  
RUN mkdir -p /home/s-mail  
RUN chown -R s-mail:s-mail /home/s-mail  
  
ENV HOME /home/s-mail  
USER s-mail  
WORKDIR /home/s-mail  
  
#CMD ["-S", "$EXIM_PORT_25_TCP_ADDR", "--syslog", "-S" "-b", "1", "-B", "1",
"-d", "30", "-k"]  
# can use schvin/exim as a linked container to use EXIM for delivery, or an
alternate SMTP server  
#CMD ["-S", "$EXIM_PORT_25_TCP_ADDR", "-b", "1", "-B", "1", "-k"]  
CMD ["-S", "127.0.0.1", "-b", "1", "-B", "1", "-k"]  
  
ENTRYPOINT ["/usr/bin/fetchmail"]  

