FROM java:8-jre  
  
MAINTAINER herloct <herloct@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
ruby \  
unzip  
  
RUN useradd -m sencha && \  
cd && cp -R .bashrc .profile /home/sencha && \  
mkdir -p /project && \  
chown -R sencha:sencha /home/sencha /project  
  
USER sencha  
ENV HOME /home/sencha  
  
RUN curl -o /home/sencha/cmd.sh.zip http://cdn.sencha.com/cmd/6.1.3/no-
jre/SenchaCmd-6.1.3-linux-amd64.sh.zip && \  
unzip -p /home/sencha/cmd.sh.zip > /home/sencha/cmd-install.sh && \  
chmod +x /home/sencha/cmd-install.sh && \  
/home/sencha/cmd-install.sh -q && \  
rm /home/sencha/cmd*  
  
ENV PATH /home/sencha/bin/Sencha/Cmd/6.1.3.42/:$PATH  
  
VOLUME /project  
WORKDIR /project  
  
EXPOSE 1841  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["help"]  

