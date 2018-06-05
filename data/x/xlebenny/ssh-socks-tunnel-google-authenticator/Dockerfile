FROM nicolasvan/ssh-socks-tunnel:latest  
  
RUN apk add --no-cache linux-pam; \  
apk add --no-cache google-authenticator; \  
sed -i 's/#ChallengeResponseAuthentication yes/ChallengeResponseAuthentication
yes/g' /etc/ssh/sshd_config; \  
su -c "google-authenticator --qr-mode=UTF8 --time-based --force --disallow-
reuse --window-size=3 --rate-limit=3 --rate-time=30 --issuer=$issuer
\--label=$label;" -s /bin/sh -l user; \  
cat /home/user/.google_authenticator;  
  
ENTRYPOINT ["entrypoint.sh"]  

