# Demonstrates how to take an insecure base image and  
# secure it through automated Polyverse protection  
# Let's build Polyscripted PHP  
FROM polyverse/polyscripted-php as polyscripted-php  
  
# Build the PHP version that our DVWA uses  
RUN ./build-php.sh  
  
# Let's start with OWASP's Damn Vulnerable Web App  
FROM polyverse/dvwa  
  
# Install polyscripted php from the first layer  
COPY \--from=polyscripted-php /polyscripted-php /polyscripted-php  
RUN yes | cp /polyscripted-php/* /  
RUN rm -rf /polyscripted-php  
  
# Let's subscribe to polymorphic Ubuntu  
RUN curl https://repo.polyverse.io/install.sh | sh -s
czcw7pjshny8lzzog8bgiizfr dvwa-demo@polyverse.io  
  
# Update all packages  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get update && apt-get -y install --reinstall $(dpkg --get-selections | awk
'{print $1}')  
  

