  
FROM bacen/sshd  
  
# repeated from sshd for clarity  
ENV USERPWD secret  
ENV PUBLICKEY ""  
ENV KEYONLY true  
EXPOSE 22  
ADD src/*.sh /opt/  
  
# install carina tool, dvm and several docker clients  
#RUN wget https://get.docker.com/builds/Linux/x86_64/docker-1.10.3.tgz -q -O
/docker.tgz && \  
# cd / && tar -xzf docker.tgz && \  
# rm /docker.tgz  
RUN chmod +x /opt/*.sh && \  
sudo -u user /opt/install-dvm.sh && \  
cp -R /home/user/.dvm /root && \  
echo "source /root/.dvm/dvm.sh" > /root/.bashrc && \  
echo "dvm use 1.10.3" >> /root/.bashrc && \  
curl -L https://download.getcarina.com/carina/latest/$(uname -s)/$(uname
-m)/carina -o /usr/local/bin/carina && \  
chmod +x /usr/local/bin/carina && \  
echo "AcceptEnv CARINA_USERNAME CARINA_APIKEY" >> /etc/ssh/sshd_config  
  
CMD ["/opt/startcarina.sh"]  

