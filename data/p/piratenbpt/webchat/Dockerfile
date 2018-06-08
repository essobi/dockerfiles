FROM piratenbpt/base  
RUN apt-get install -y python python-twisted python-twisted-bin python-
twisted-core python-twisted-runner python-twisted-names python-twisted-mail
python-twisted-words python-twisted-web python-zope.interface python-openssl
openjdk-6-jdk mercurial  
RUN hg clone http://hg.qwebirc.org/qwebirc/ /qwebirc  
ADD qwebirc-password.patch /qwebirc/password.patch  
ADD qwebirc-config.py.sample /qwebirc/config.py.sample  
RUN cd /qwebirc; hg up -C stable; hg import --no-commit password.patch  
ADD startup.sh /startup.sh  
EXPOSE 80/tcp  
CMD /startup.sh  

