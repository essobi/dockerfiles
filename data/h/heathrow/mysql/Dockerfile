FROM mysql:5.6  
ENV ENTRYKIT_VERSION 0.4.0  
ADD
https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz
/tmp/entrykit.tgz  
RUN tar -xzf /tmp/entrykit.tgz -C /bin entrykit \  
&& entrykit --symlink \  
&& rm /tmp/entrykit.tgz  
  
COPY ./runtime.cnf.tmpl /etc/mysql/conf.d/runtime.cnf.tmpl  
  
ENTRYPOINT ["render", "/etc/mysql/conf.d/runtime.cnf", "--", "docker-
entrypoint.sh"]  
CMD ["mysqld"]  

