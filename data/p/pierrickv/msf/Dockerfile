FROM debian:stretch-slim  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update -qq && apt-get install --assume-yes --force-yes \  
curl \  
git \  
gnupg \  
nmap \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl https://raw.githubusercontent.com/rapid7/metasploit-
omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb >
msfinstall \  
&& chmod 755 msfinstall \  
&& ./msfinstall \  
&& rm ./msfinstall \  
&& apt-get autoremove --assume-yes --force-yes \  
curl \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["msfconsole"]  

