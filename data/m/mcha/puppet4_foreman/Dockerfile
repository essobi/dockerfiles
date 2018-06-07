#  
# Create an image with Foreman + Puppet 4.x within  
#  
# @See : https://www.theforeman.org/manuals/1.14/index.html  
# @author : Michel CHA  
FROM debian  
  
WORKDIR /root  
  
#ENV VARNAME value  
# Shell form to run command -> will interpret variable defined with ENV  
# RUN execute the command in a new layer -> recommended for tool installation  
# Multiple RUN is possible  
# Avoid the use of ADD => unpredictable  
# Update packages && install tooling packages  
RUN echo "deb http://deb.theforeman.org/ jessie 1.14" >
/etc/apt/sources.list.d/foreman.list \  
&& echo "deb http://deb.theforeman.org/ plugins 1.14" >>
/etc/apt/sources.list.d/foreman.list \  
&& apt-get update \  
&& apt-get -y install ca-certificates wget vim locales ntp locate  
  
# Compile needed locale for Foreman setup  
COPY resources/etc/locale.gen /etc/locale.gen  
RUN locale-gen en_US.utf8 && locale-gen fr_FR.utf8  
  
# Setup NTP  
COPY resources/etc/ntp.conf /etc/ntp.conf  
RUN service ntp restart  
  
# Retrieve puppet 4.x repos information  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-jessie.deb \  
&& dpkg -i puppetlabs-release-pc1-jessie.deb  
RUN rm -f puppetlabs-release-pc1-jessie.deb  
# Get the foreman installer => installation should be done inside running
container  
RUN wget -q http://deb.theforeman.org/pubkey.gpg -O- | apt-key add - \  
&& apt-get update && apt-get -y install foreman-installer  
  
# Setup to be finished inside running container by using ./setup_foreman.sh  
# So that fqdn is setup properly  
COPY resources/setup_foreman.sh /root/setup_foreman.sh  
COPY resources/services.sh /root/services.sh  
COPY resources/start.sh /root/start.sh  
  
RUN chmod u+x /root/setup_foreman.sh /root/services.sh /root/start.sh  
  
# Other resources  
COPY resources/.bashrc /root/.bashrc  
COPY resources/create_dbuser.sql /root/create_dbuser.sql  
  
# Port exposed  
## Apache  
EXPOSE 443  
## Postgresql  
EXPOSE 5432  
# Exec form to run command -> will not interpret variable defined with ENV  
# Exec form is recommanded for CMD and ENTRYPOINT  
# CMD is used to specify a default command to run (only one CMD per
Dockerfile)  
CMD ["/root/start.sh"]  
  
# When CMD is mixed with ENTRYPOINT  
# Then CMD's value provide the args to the command in ENTRYPOINT  
# This ensure a parameterized ENTRYPOINT  
# Ex : docker run image_alias yyy  
# will result in xxx yyy  
#ENTRYPOINT ["xxx"]  

