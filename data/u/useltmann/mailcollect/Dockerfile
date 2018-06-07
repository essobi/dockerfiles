### install debian ###  
FROM debian:8  
MAINTAINER seltmann@ub.uni-leipzig.de  
EXPOSE 25 143  
VOLUME ["/home/dev/Maildir"]  
ENTRYPOINT ["/docker/init"]  
CMD ["run"]  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD assets/build /docker/build  
ADD assets/setup /docker/setup  
ADD assets/init /docker/init  
  
RUN apt-get update \  
&& apt-get install -y supervisor postfix dovecot-imapd procmail \  
&& apt-get autoclean \  
&& apt-get clean \  
&& chmod 755 /docker/build/init /docker/init  
  
RUN /docker/build/init

