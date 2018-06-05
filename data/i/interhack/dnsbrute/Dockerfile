FROM python:2.7-alpine  
MAINTAINER interhack  
  
RUN apk update && apk add ca-certificates && update-ca-certificates && apk add
openssl  
RUN pip install https://github.com/interhack86/dnsbrute/archive/master.zip  
RUN mkdir domains  
WORKDIR domains  
RUN wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/bitquark-
subdomains-top100K.txt && \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/deepmagic.com-
top500prefixes.txt && \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/deepmagic.com-
top50kprefixes.txt && \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/fierce-
hostlist.txt && \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/namelist.txt
&& \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/sortedcombied-
knock-dnsrecon-fierce-reconng.txt && \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-
top1mil-110000.txt && \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-
top1mil-20000.txt && \  
wget
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-
top1mil-5000.txt  
  
ENTRYPOINT ["python", "-m", "dnsbrute"]

