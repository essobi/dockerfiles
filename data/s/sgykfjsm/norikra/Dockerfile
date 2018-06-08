FROM sgykfjsm/jruby:latest  
MAINTAINER shigeyuki.fujishima_at_gmail.com  
  
#  
ENV CONTAINER_NAME norikra  
ENV NORIKRA_DIR /opt/norikra  
  
# networking  
EXPOSE 26578  
# td-agent and more  
## To install norikra, I need 'rbenv shell'.  
## so, I have to read bash-profile by `/bin/bash -l -c`.  
## JRUBY_VERSION is environment variable from sgykfjsm/ruby.  
RUN /bin/bash -l -c "rbenv shell ${JRUBY_VERSION} && gem install norikra
--platform jruby --no-document --quiet" \  
&& useradd norikra --shell /bin/false -M \  
&& mkdir -m 755 -p "${NORIKRA_DIR}/log" "${NORIKRA_DIR}/out"
"${NORIKRA_DIR}/stats"  
COPY opt/norikra/norikra.sh /opt/norikra/norikra  
  
# finish  
CMD ["/opt/norikra/norikra", "start"]  

