FROM illallangi/ansible:latest  
ENV WEBTREES_VERSION=1.7.9  
ENV
WEBTREES_SHA256=9eebfefff250135bf68a07a5e7a2693919cec596d756f60762d38a18ede79c31  
COPY image/* /etc/ansible.d/image/  
COPY emjay-1.7.9.tar.gz /usr/local/src/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV USER=webtrees  
ENV UID=1024  
ENV WEBTREES_SERVERPORT=8100  
ENV WEBTREES_DB_PORT=3306  
ENV WEBTREES_DB_PREFIX=wt_  
ENV WEBTREES_LANG=en-US  
ENV WEBTREES_PATH=/var/lib/webtrees/data  
ENV WEBTREES_MAXFILESIZE=20M  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/webtrees-entrypoint.sh"]  

