FROM runningman84/cgate:latest  
MAINTAINER a.mayr@adito.de  
  
# copy tweaked admin account (postmaster/xxxx) and use the dash skin to
prevent severe brain damage  
COPY ./src/Accounts/postmaster.macnt/
/var/CommuniGate/Accounts/postmaster.macnt/  
# copy testuser data  
COPY ./src/Accounts/testuser.macnt/ /var/CommuniGate/Accounts/testuser.macnt/  
COPY ./src/Accounts/testuser2.macnt/
/var/CommuniGate/Accounts/testuser2.macnt/  
COPY ./src/Accounts/Settings/access.settings
/var/CommuniGate/Accounts/Settings/access.settings  
# copy settings (domain)  
COPY ./src/Settings/Main.settings /var/CommuniGate/Settings/Main.settings  
COPY ./src/Directory/Main.data /var/CommuniGate/Directory/Main.data  

