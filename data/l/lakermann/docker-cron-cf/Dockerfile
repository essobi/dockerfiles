FROM python:2.7  
MAINTAINER lakermann  
  
# Add cloudfoundrycli  
ADD "https://cli.run.pivotal.io/stable?version=6.34.1&release=linux64-binary"
/tmp/  
  
# Setup cloudfoundrycli  
RUN cat /tmp/stable | tar xfz - -C /usr/bin && \  
chmod ugo+rx /usr/bin/cf  
  
# Install cloudfoundry statistics plugin  
RUN /usr/bin/cf install-plugin Statistics -r CF-Community -f  
  
# Need hg to download devcron  
RUN apt-get update && apt-get install -y mercurial  
  
# Yay devcron  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
  
# Setup defaults devcron  
RUN mkdir /cron && \  
echo "* * * * * /cron/sample.sh" > /cron/crontab && \  
echo "echo hello world" > /cron/sample.sh && \  
chmod a+x /cron/sample.sh  
  
VOLUME ["/cron"]  
  
CMD ["devcron.py", "/cron/crontab"]  

