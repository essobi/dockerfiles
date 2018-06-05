# docker run -ti -e EMAIL="your@email.com" -e NAME="Your Name"
boris/mutt:latest  
FROM debian:jessie  
  
MAINTAINER Boris Quiroz <boris@insert-coin.org>  
  
RUN groupadd -g 1000 user \  
&& useradd --create-home -d /home/user -g user -u 1000 user  
  
# Uncomment in case you use mailcap  
#RUN mkdir /home/user/tmp ; chown -R user:user /home/user/tmp  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
mutt-patched \  
# elinks \  
vim \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
USER user  
ENV HOME /home/user  
RUN mkdir -p $HOME/.mutt/cache/bodies $HOME/.mutt/cache/headers && touch
$HOME/.mutt/certificates  
  
COPY entrypoint.sh /entrypoint.sh  
COPY mutt-files $HOME/.mutt  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mutt-patched", "-F", "~/.mutt/muttrc"]  

