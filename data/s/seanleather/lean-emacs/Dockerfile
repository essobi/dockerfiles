FROM seanleather/lean  
MAINTAINER Sean Leather <https://github.com/spl>  
  
# Install the required packages  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk --no-cache add emacs@testing  
  
# Download and install Emacs packages needed for Lean  
WORKDIR /root  
COPY configure-lean-mode.el ./  
RUN emacs --script configure-lean-mode.el  
  
ENTRYPOINT ["emacs"]  

