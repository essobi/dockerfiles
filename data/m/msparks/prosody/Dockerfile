FROM ubuntu:14.04  
MAINTAINER Matt Sparks <ms@quadpoint.org>  
  
# Install prosody.  
RUN apt-get update && \  
apt-get install -y curl && \  
curl https://prosody.im/files/prosody-debian-packages.key \  
| apt-key add - && \  
echo deb http://packages.prosody.im/debian $(lsb_release -sc) main \  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y prosody && \  
apt-get remove -y curl && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN chown prosody:prosody /var/run/prosody  
  
# Add default configuration files.  
ADD conf/ /etc/prosody  
  
# Set up example.com certificates. localhost.{key,crt} are created by the  
# installation step above.  
RUN ln -s /etc/prosody/certs/localhost.key /etc/prosody/certs/example.com.key  
RUN ln -s /etc/prosody/certs/localhost.crt /etc/prosody/certs/example.com.crt  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["prosodyctl", "start"]  

