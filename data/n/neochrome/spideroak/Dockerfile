# vim: ft=dockerfile  
FROM centos:7  
MAINTAINER Johan Stenqvist <johan@stenqvist.net>  
LABEL Description="SpiderOAK client"  
  
RUN \  
curl -Ls 'https://spideroak.com/getbuild?platform=fedora&arch=x86_64' -o
spideroak.rpm \  
&& rpm -i spideroak.rpm \  
&& rm -f spideroak.rpm \  
&& curl -Ls
https://github.com/neochrome/lsdvol/releases/download/v0.2.1/lsdvol -o
/bin/lsdvol \  
&& chmod +x /bin/lsdvol  
  
COPY ./run.sh .  
ENTRYPOINT ["./run.sh"]  
CMD ["--headless"]  

