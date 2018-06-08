From ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y git sudo make locate wget ruby-dev host gem
bsdmainutils|| true  
RUN git clone https://github.com/gauntlt/gauntlt /opt/gauntlt  
RUN git clone https://github.com/drwetter/testssl.sh.git /opt/testssl  
RUN /bin/bash -c "cd /opt/gauntlt; source ./install_gauntlt_deps.sh"; exit 0  
RUN bash /opt/gauntlt/ready_to_rumble.sh  
RUN pip install datadog  
RUN pip install qualysapi  

