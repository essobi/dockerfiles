# LEDStatus  
# https://github.com/alexwitherspoon/ledstatus  
FROM alexwitherspoon/debian  
  
MAINTAINER Alex Witherspoon <alex@alexwitherspoon.com>  
  
# Commands to Stage OS  
RUN echo "Installing Base Utilties" && \  
bash -c "apt-get update -qq" && \  
bash -c "apt-get install -qq --force-yes python sudo curl cron git nano" && \  
bash -c "echo 'root:ledstatus' | chpasswd" && \  
bash -c "apt-get autoremove -qq --force-yes" && \  
bash -c "apt-get clean -qq --force-yes" && \  
echo "Base Utilities Installed" && \  
echo "...."  
  
RUN echo "Installing Hue-shell" && \  
bash -c "OPT=install; $(curl -fksSkL http://raw.github.com/Josef-
Friedrich/Hue-shell/master/install.sh)" && \  
echo "Hue-shell Installed" && \  
echo "...."  
  
RUN echo "Installing ledstatus app" && \  
bash -c "git clone https://github.com/alexwitherspoon/ledStatus.git
/opt/ledstatus" && \  
bash -c "crontab /opt/ledstatus/ledstatus.cron" && \  
bash -c "chmod +x /opt/ledstatus/run.sh" && \  
bash -c "touch /var/log/ledstatus.log" && \  
echo "ledstatus app" && \  
echo "...."  
  
# Commands to Run App  
CMD bash -c "cron" && \  
bash -c "sleep 1d"  

