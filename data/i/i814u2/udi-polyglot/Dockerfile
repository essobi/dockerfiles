FROM jfloff/alpine-python:2.7  
ARG binfile=polyglot.linux.x86_64.pyz  
ARG user=polyglot  
ARG group=polyglot  
ARG uid=1000  
ARG gid=1000  
RUN addgroup -g ${gid} ${group} \  
&& adduser -h /home/${user} -s /bin/sh -G ${group} -D -u ${uid} ${user}  
  
WORKDIR /home/${user}  
COPY custom.txt .  
  
RUN pip install --upgrade pip  
  
RUN mkdir Polyglot && wget
https://github.com/UniversalDevicesInc/Polyglot/raw/unstable-
release/bin/${binfile} -P Polyglot  
COPY pip-upgrade-all.py ./Polyglot  
COPY startup.sh ./Polyglot  
COPY file.arch ./Polyglot  
RUN chown -R ${user}:${group} /home/${user} \  
&& chmod 755 /home/${user}/Polyglot/${binfile} \  
&& chmod 755 /home/${user}/Polyglot/startup.sh  
  
USER ${user}  
RUN pip install --user -r
https://raw.githubusercontent.com/UniversalDevicesInc/Polyglot/unstable-
release/requirements.txt \  
&& while read line; do $line; done < custom.txt  
WORKDIR /home/${user}/Polyglot  
ENTRYPOINT ["./startup.sh"]  

