FROM jenkins  
  
# Install rbenv dependencies  
USER root  
RUN apt-get update && apt-get install -y autoconf bison build-essential
libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev
libgdbm3 libgdbm-dev  
# Add dummy user to fix UID 1000 issue  
RUN groupadd -g 10000 gituser && useradd -d /var/jenkins_home -u 10000 -g
10000 -m -s /bin/bash gituser  
USER jenkins  
  

