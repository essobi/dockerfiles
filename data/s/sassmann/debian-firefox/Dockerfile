FROM debian:unstable  
SHELL ["/bin/bash", "-c"]  
  
#RUN sed -i '0,/RE/s/main/main contrib/' /etc/apt/sources.list  
RUN printf 'path-exclude=/usr/share/locale/*\npath-
exclude=/usr/share/doc/*\npath-include=/usr/share/locale/en/*' >
/etc/dpkg/dpkg.cfg.d/purge  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
firefox wget libcurl3 libnspr4 libnss3 libpango1.0 libcanberra-gtk3-module
packagekit-gtk3-module libgl1-mesa-dri libvdpau-va-gl1 va-driver-all fonts-
dejavu pulseaudio fonts-noto-cjk icedtea-netx \  
&& wget -A amd64.deb -e robots=off -m -p -E -k -K -np http://www.deb-
multimedia.org/pool/non-free/f/flash-player/ \  
&& dpkg -i www.deb-multimedia.org/pool/non-free/f/flash-player/flashplayer-
mozilla* \  
&& rm -rf /tmp/* /var/{tmp,cache}/* /var/lib/{apt,dpkg}/  
RUN mkdir -p /etc/firefox/  
RUN echo -e '\  
pref("browser.crashReports.unsubmittedCheck.autoSubmit", true);\n\  
pref("browser.startup.homepage","data:text/plain,browser.startup.homepage=https://www.startpage.com");\n\  
pref("datareporting.healthreport.service.firstRun", false);\n\  
pref("datareporting.healthreport.uploadEnabled", false);\n\  
pref("datareporting.policy.dataSubmissionPolicyBypassNotification", true);\n\  
pref("reader.parse-on-load.enabled", false);\n\  
pref("signon.rememberSignons", false);\n\  
pref("toolkit.telemetry.reportingpolicy.firstRun", false);\n'\  
>> /etc/firefox/syspref.js  
#FIXME: does not stick  
#pref("browser.search.widget.inNavBar", true);\n\  
RUN adduser --disabled-password user --gecos "User"  
USER user  
ENV HOME /home/user  
ENV PULSE_SERVER unix:/tmp/pulse  
  
CMD ["firefox","--new-instance","about:blank"]  

