FROM phusion/baseimage:latest  
  
LABEL maintainer="totentech@gmail.com"  
  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y wget curl python mercurial git sqlite3 mlocate sudo apt-
utils mc vim screen man python-software-properties colordiff bash-completion
apt-file apt-transport-https ca-certificates mono-complete traceroute net-
tools && \  
apt-key adv \--keyserver hkp://ha.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install -y docker-engine=1.11.1-0~xenial docker-compose && \  
bash -c "`curl -sL
https://raw.githubusercontent.com/michaelsauter/crane/master/download.sh`" &&
sudo mv crane /usr/local/bin/crane && \  
adduser \--disabled-password \--gecos "" totentanz && \  
echo "totentanz\tALL=(ALL:ALL) NOPASSWD: ALL\n" > /etc/sudoers.d/totentanz &&
\  
chmod 0440 /etc/sudoers.d/totentanz && \  
mkdir /home/totentanz/.ssh && \  
chown totentanz:totentanz /home/totentanz/.ssh && \  
chmod 0770 /home/totentanz/.ssh && \  
echo "colorscheme elflord" > /home/totentanz/.vimrc && \  
echo "syntax on" >> /home/totentanz/.vimrc && \  
echo "set hlsearch" >> /home/totentanz/.vimrc && \  
echo "set so=7" >> /home/totentanz/.vimrc && \  
echo "set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{CurDir()}%h\ \ \
Line:\ %l/%L:%c" >> /home/totentanz/.vimrc && \  
echo "set number" >> /home/totentanz/.vimrc && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABJQAAAQEAyI9kyK38w289PbyEoioHd25G581OpZYekhgO2guhLjSj36/Cxrcxz7o+GhGv4BMFSt85cSfDYKOBJm+IyRFkJyjFdsUNzWk02gcSFdMUhccxErqMfE2jZrK3KU3hrpN5i9OhK7CzgycAgRlTd7ujWQw+DuvB6kc8DJh6tqMbYZ52gG1j8JWuGY8ebUo+y+PZ315oFlp+NRCtqkZsuIYaAriiB4WqH4xxjNEIXHhJ+1zqiB3XN2lCGnj5/a5vih8UX1Tb3BjJmfkYrE1n9S5MGFan1QL16Pjlj3dIypR65v+q8oWnwWIdPknNwmgm6iREg6DaT3V+mNTzH3/cUYHB5w==
Totentanz@TOTENTANZ-PC" >> /home/totentanz/.ssh/authorized_keys && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDpNs2xeG8zNYQbXkoUj+Ry4XQ06bjaH/gR5HEzz9GFDpeW8r/nnO4A4Ii2AU8EOHEcUxJtsjmSzYZD2/q4h1dhZDQHjapuzMtH/QlQtiJBMvROvu64R5M6r7OYXmynVPUere7SPp4LK34YAJ5RypGx9obnS/Nh9htoCLX6/u9clZ/6odrwzTR9VV7w5koqasNRQKsiYvwx9R/4mcF0Hy5HCB/in/wMQY0DmMeCx12Fzksqt9cz8RW0Eq6WRRQwkh7IprMxx7I5dEqcVNbarhdMCS7bXvbHhQHgW47tchEEfutdxmmUCfhSXy4IdXtY8iK9tXnLLIsJg378+nqq/g2b
Totentanz@IPHONE" >> /home/totentanz/.ssh/authorized_keys && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABJQAAAQEAkaGizMkFM8Qm3wXHnC46/Q+Ccx7yP45Y8ZIXSoqYXnoF7R9VCj5t/xbSnmOi2hp5kaVs74qSnDwrTdz8z7OyVKbK6r+6muAcfYBGkDkA3P++Eq+iGlVCknyvaFkot+uczpODyU6kmYdTmA7olHg1+3SEO4KWwMU/Ood57Ep6bEh9wj8GkzxhABIrPUiTYs+aHEXW1amQ4H20RXOcSpAv8sjhPpsKBZ+RMpMZISzhDX6kmR0YGnQotdkPi33eekWJivtO6qzevky0qZ9yyblEL9h8WkGkzdxyoZ+c45aKjIp9j9R6ltBOGNg+q09YK8g1jYt5JK9cCu5XUpekLYic1w==
Totentanz@CAPSULE" >> /home/totentanz/.ssh/authorized_keys && \  
rm -f /etc/service/sshd/down && \  
sudo -u totentanz -H mkdir /home/totentanz/dev && \  
sudo -u totentanz -H git clone https://github.com/banga/powerline-shell
/home/totentanz/dev/powerline-shell && \  
cd /home/totentanz/dev/powerline-shell && \  
sudo -u totentanz -H ./install.py && \  
echo "function _update_ps1() { PS1=\"\$(~/dev/powerline-shell/powerline-
shell.py \$? 2> /dev/null)\"; }" >> /home/totentanz/.bashrc && \  
echo "if [ \"\$TERM\" != linux ]; then PROMPT_COMMAND=\"_update_ps1;
\$PROMPT_COMMAND\"; fi" >> /home/totentanz/.bashrc && \  
chown totentanz:totentanz /home/totentanz/.bashrc  

