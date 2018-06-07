FROM selenium/node-firefox:3.7.1-beryllium  
  
USER root  
  
# install xvfb  
RUN apt-get update && \  
apt-get install -y xvfb git && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
COPY xvfb /etc/init.d/xvfb  
RUN chmod +x /etc/init.d/xvfb  
  
RUN echo "sudo service xvfb start" >> /etc/bash.bashrc  
ENV DISPLAY :99  
RUN mkdir -p /katalon  
WORKDIR /katalon  
  
COPY katalon_studio_linux_64 /katalon  
RUN chmod +x
/katalon/configuration/resources/drivers/chromedriver_linux64/chromedriver
/katalon/configuration/resources/drivers/firefox_linux64/geckodriver  
  
RUN ln -s /katalon/katalon /usr/bin/katalon && chown seluser /usr/bin/katalon  
  
COPY start_xvfb.sh /start_xvfb.sh  
RUN chmod +x /start_xvfb.sh  
  
RUN chown -R seluser /katalon && chmod o+x /katalon/katalon  
  
USER seluser  
  
CMD ["/start_xvfb.sh"]

