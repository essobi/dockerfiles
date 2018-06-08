FROM dustin/tiny  
MAINTAINER Mitchell Monahan, soccermitchy@gmail.com, best way to contact me is
via IRC, irc.esper.net, PM me (my nick is wolfmitchell)  
# Update local package index, the image doesn't contain it.  
RUN apt-get update  
  
# Install our packages  
RUN apt-get install -y lua5.1 luarocks git nano  
  
# Install luasocket  
RUN luarocks install luasocket  
  
# Install bit32  
RUN luarocks install bit32  
  
# Clone repo  
RUN git clone http://github.com/soccermitchy/mitchbot.git /usr/local/mitchbot  
  
# A notice for the user  
#RUN echo "You will need to configure MitchBot for first run before running
the container."  
#RUN echo "The configuration file is expected to be
/usr/local/mitchbot/config.lua"  
#RUN echo "An example config is in /usr/local/mitchbot/config.lua.example"  
# Set some important stuff...  
USER daemon  
ENTRYPOINT ["lua","-e","\"if not io.popen('/usr/local/mitchbot/config.lua')
then print('You need to configure mitchbot. There is an example config in
/usr/local/mitchbot/config.example.lua. The config is expected to be in
/usr/local/mitchbot/config.lua/') else dofile'/usr/local/mitchbot/main.lua'
end\""]

