FROM microsoft/dotnet:2.0-sdk  
MAINTAINER Robbert van der Helm <mail@robbertvanderhelm.nl>  
  
# Compiling and testing the application depends on Node.js and some Python  
# modules  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs python3 python3-pip zip \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g yarn  
  
# We need ripgrep for finding lines that are too long  
RUN curl -LO
https://github.com/BurntSushi/ripgrep/releases/download/0.8.1/ripgrep_0.8.1_amd64.deb
\  
&& dpkg -i ripgrep_0.8.1_amd64.deb \  
&& rm ripgrep_0.8.1_amd64.deb  
  
# Since the Python dependencies tend to change we'll install them at run time,  
# but we can atleast preinstall testing and static analysis related tools  
RUN pip3 install flake8 pytest  

