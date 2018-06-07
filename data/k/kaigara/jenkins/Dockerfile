FROM jenkins:latest  
  
# Install Kaigara  
USER root  
RUN curl -sL https://kaigara.org/get | sh  
USER jenkins  
  
RUN /usr/local/bin/install-plugins.sh \  
kubernetes \  
workflow-aggregator \  
credentials-binding \  
git \  
ldap \  
gerrit-trigger \  
google-login  
  
COPY operations /opt/kaigara/operations  
COPY resources /etc/kaigara/resources  
  
RUN mkdir -p /usr/share/jenkins/ref/secrets/ \  
&& echo "false" > /usr/share/jenkins/ref/secrets/slave-to-master-security-
kill-switch  
  
ENTRYPOINT ["kaigara"]  
CMD ["start", "jenkins.sh"]  

