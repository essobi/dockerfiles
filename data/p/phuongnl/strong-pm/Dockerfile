FROM node  
  
MAINTAINER PhuongNL "phuongnl.hn@gmail.com"  
RUN useradd -ms /bin/bash strong-pm \  
&& chown -R strong-pm:strong-pm /usr/local \  
&& su strong-pm -c "npm install -g strong-pm && npm cache clear"  
  
# Set up some semblance of an environment  
WORKDIR /home/strong-pm  
ENV HOME=/home/strong-pm  
  
# Run as non-privileged user inside container  
USER strong-pm  
  
# Expose strong-pm port  
EXPOSE 8701 3001-3020  
ENTRYPOINT ["sl-pm", "-b", ".", "-l", "8701"]  

