FROM debian:jessie  
MAINTAINER AJ Bowen <aj@soulshake.net>  
  
RUN apt-get update && apt-get install -y \  
python \  
python-pip \  
python-docutils  
  
RUN pip install gandi.cli  
  
ENTRYPOINT [ "gandi" ]  
  
# Optional: install manpages so we can run 'man gandi' on the host  
# Make sure to bindmount a location contained in the host's `manpath` at run
time, e.g.:  
# -v /usr/share/man  
RUN apt-get install -y wget man  
RUN wget
https://raw.githubusercontent.com/Gandi/gandi.cli/master/gandicli.man.rst  
RUN rst2man --no-generator gandicli.man.rst > $HOME/gandi.1.man  
RUN install -g 0 -o 0 -m 0644 $HOME/gandi.1.man /usr/local/man  
RUN gzip /usr/local/man/gandi.1.man  
RUN mkdir /usr/local/man/man1  
RUN mv /usr/local/man/gandi.1.man.gz /usr/local/man/man1/gandi.1.gz  
  
# Run command:  
# docker run -v ~/.config/gandi/config.yaml:/root/.config/gandi/config.yaml
soulshake/gandi domain list  

