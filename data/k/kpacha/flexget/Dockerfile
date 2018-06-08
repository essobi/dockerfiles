FROM cptactionhank/flexget  
  
RUN pip install -I subliminal \  
&& easy_install periscope  
  
RUN mkdir -p /root/flexget /root/.config /shows /transmission  
  
COPY start.sh /root/flexget/start.sh  
COPY config_base.yml /root/flexget/config_base.yml  
  
ENV SUBTITLE_LANGUAGE="en"  
ENV RSS_URL="noop"  
ENTRYPOINT ["/root/flexget/start.sh"]  
CMD ["--loglevel", "debug", "daemon", "start"]

