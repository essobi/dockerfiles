FROM debian:jessie-slim  
LABEL description="Cron runner"  
LABEL maintainer="todd.mannherz@gmail.com"  
  
RUN apt-get update && \  
apt-get install -qqy apt-transport-https ca-certificates cron curl gnupg2
software-properties-common --no-install-recommends  
  
# Install Docker  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - &&
\  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get install -qqy docker-ce  
  
# Docker logging from cron runs  
RUN ln -sf /proc/1/fd/1 /var/log/cron.log  
  
COPY runner.sh /runner.sh  
RUN chmod +x /runner.sh  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

