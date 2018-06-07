FROM dougbtv/asterisk13  
MAINTAINER Dorinel Filip <dorinel.filip@beia.ro>  
  
# Expose port for ARI (Asterisk Rest Interface)  
EXPOSE 8088  
# Install Python3 and jinja2 for the run_asterisk.py script  
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm  
RUN yum -y install python36u python36u-pip  
RUN pip3.6 install jinja2  
  
# Install dependecies for GoogleTTS AGI  
RUN yum -y install perl perl-libwww-perl perl-LWP-Protocol-https sox mpg123  
  
# Create /srv/asterisk directory  
RUN mkdir -p /srv/asterisk/templates  
  
# Copy run script and configuration templates  
WORKDIR /srv/asterisk  
COPY run_asterisk.py .  
COPY templates/* templates/  
  
# Copy non-template configuration file  
COPY config/* /etc/asterisk/  
  
# Install GoogleTLS AGI  
WORKDIR /var/lib/asterisk/agi-bin/  
RUN curl -O https://raw.githubusercontent.com/zaf/asterisk-
googletts/master/googletts.agi  
RUN chmod +x googletts.agi  
  
# Set the working directory back to /  
WORKDIR /  
  
# Overwrite the entrypoint of the container  
ENTRYPOINT python3.6 /srv/asterisk/run_asterisk.py  

