FROM urgemerge/chromium-
pulseaudio@sha256:21d8120ff7857afb0c18d4abf098549de169782e652437441c3c7778a755e46f  
RUN \  
adduser --disabled-password --gecos "" user && \  
chown user:user /data && \  
apt-get clean all  
USER user  
WORKDIR /home/user  
ENTRYPOINT ["chromium", "--user-data-dir=/data"]  
CMD []

