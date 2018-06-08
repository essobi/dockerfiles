FROM debian  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends curl gnupg apt-transport-https
ca-certificates \  
&& curl -s https://updates.signal.org/desktop/apt/keys.asc | apt-key add - \  
&& echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main"
> /etc/apt/sources.list.d/signal-xenial.list \  
&& apt-get update \  
&& apt-get install -yq --no-install-recommends libx11-xcb1 libasound2 signal-
desktop \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN adduser --disabled-password user --gecos "User"  
USER user  
ENV HOME /home/user  
ENV PULSE_SERVER unix:/tmp/pulse  
  
RUN mkdir -p /home/user/.config/Signal  
  
CMD ["signal-desktop"]  

