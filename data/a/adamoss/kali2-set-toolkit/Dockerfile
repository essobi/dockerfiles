####################################################  
# YOU CAN USE adamoss/kali2-base if you wish ##  
####################################################  
FROM officialkali/kali:2.0  
MAINTAINER Adam Ossenford <AdamOssenford@gmail.com>  
####################################################  
# UPDATE APT AND INSTALL THE METASPLOIT FRAMEWORK  
####################################################  
RUN apt-get update -y && apt-get upgrade -y && apt-get install metasploit-
framework python-crypto python-pexpect -y && msfupdate  
####################################################  
# CUSTOMIZE METASPLOIT BANNER TO SOMETHING SECKC  
####################################################  
RUN rm /usr/share/metasploit-framework/data/logos/*.txt  
COPY seckc-docker.txt /usr/share/metasploit-framework/data/logos/cowsay.txt  
####################################################  
# SOMETIMES THE DATABASE SUCKS SO RESTART IT NOW  
####################################################  
RUN service postgresql restart  
####################################################  
# Add bitbuckets key  
####################################################  
RUN mkdir -p /root/.ssh/ && ssh-keyscan bitbucket.org >>
/root/.ssh/known_hosts  
####################################################  
# install SET from github  
####################################################  
WORKDIR "/usr/local/"  
RUN git clone https://github.com/trustedsec/social-engineer-toolkit.git  
WORKDIR "/usr/local/social-engineer-toolkit"  
###################################################  
# WE IMPLY THAT AGREEMENTS WILL BE MADE  
####################################################  
RUN sed -i 's/.*Do you agree to the terms of service.*/ choice = \"y\"/g'
setoolkit  
##############################  
# ENTER SET DOJO ###  
##############################  
CMD cat /usr/share/metasploit-framework/data/logos/cowsay.txt && sleep 2 && cd
/usr/local/social-engineer-toolkit/; ./setoolkit  

