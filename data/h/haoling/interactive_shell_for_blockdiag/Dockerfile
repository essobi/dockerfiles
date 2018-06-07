FROM python:2.7-jessie  
RUN apt-get update &&\  
apt-get install -y fonts-ipafont mercurial unzip &&\  
apt-get -y autoremove &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
RUN mkdir /app &&\  
cd /app &&\  
hg clone https://bitbucket.org/blockdiag/blockdiag_interactive_shell &&\  
cd blockdiag_interactive_shell &&\  
python bootstrap.py &&\  
bin/buildout  
RUN cd /app/blockdiag_interactive_shell/app &&\  
unzip -d distlib distlib.zip  
RUN cd /app/blockdiag_interactive_shell/app && pip install pillow  
RUN echo opt_in: false > /root/.appcfg_nag &&\  
echo timestamp: 0.0 >> /root/.appcfg_nag  
VOLUME ["/work"]  
WORKDIR /work  
EXPOSE 8080 8000  
CMD ["/app/blockdiag_interactive_shell/bin/dev_appserver","--host","0.0.0.0","
--admin_host","0.0.0.0","/app/blockdiag_interactive_shell/app"]  

