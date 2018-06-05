# to build  
# docker build -t aptly:ubuntu-trusty .  
# Then run (this will use a /tmp/aptly dir for the data!):  
# mkdir -p /tmp/aptly && docker run -it -v /tmp/:/var/aptly -p 80:80 aptly
aptly  
# serve --listen=":80"  
FROM ubuntu:trusty  
MAINTAINER Joseph Herlant <herlantj@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://repo.aptly.info/ squeeze main" >
/etc/apt/sources.list.d/aptly.list && \  
gpg --keyserver keys.gnupg.net --recv-keys 9E3E53F19C7DE460 && \  
gpg -a --export 9E3E53F19C7DE460 | sudo apt-key add - && \  
apt-get update && apt-get -y install aptly  
  
ADD aptly.conf /etc/aptly.conf  
VOLUME ["/var/aptly"]  
EXPOSE 80  
# The init of the aptly is defined in this script:  
COPY ./docker_entrypoint_aptly.sh /  
ENTRYPOINT [ "/docker_entrypoint_aptly.sh" ]  
RUN chmod u+x /docker_entrypoint_aptly.sh  
  
CMD [ "aptly", "serve", "--listen=\":80\" ]  

