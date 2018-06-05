FROM microsoft/dotnet:latest  
LABEL maintainer "brad@bjc.id.au"  
  
# Download and install, su-exec. https://github.com/ncopa/su-exec  
# This is a simple tool that will simply execute a program with different
privileges.  
# The program will not run as a child, like su and sudo, so we work around TTY
and signal issues.  
RUN curl -fsSLR -o /usr/local/bin/su-exec \  
https://github.com/javabean/su-exec/releases/download/v0.2/su-exec.$(dpkg
--print-architecture | awk -F- '{ print $NF }') && \  
chmod +x /usr/local/bin/su-exec  
  
# Setup our custom entry point which will use su-exec  
# to run the requested command as the host's user.  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

