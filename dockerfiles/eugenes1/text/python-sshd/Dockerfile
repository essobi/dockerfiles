FROM python:2.7-alpine
MAINTAINER Eugene Savchenko

ENV PROJECT_PATH /usr/src/python-app/
ENV VENV_PATH /root/venv/
ENV SSH_SERVER_KEYS /etc/ssh/host_keys/

#
# Install virtualenv for developing
#
RUN pip install --no-cache-dir virtualenv

#
# Copy rootfs files
#
COPY /rootfs /

#
# Install ssh-server for connect remote python interpreter
#
EXPOSE 22
RUN apk update && \
    apk add bash openssh sudo && \
    mkdir -p ${SSH_SERVER_KEYS} && \
    mkdir ${PROJECT_PATH} && \
    echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_rsa_key" >> /etc/ssh/sshd_config && \
    echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_dsa_key" >> /etc/ssh/sshd_config && \
    echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_ecdsa_key" >> /etc/ssh/sshd_config && \
    echo -e "HostKey ${SSH_SERVER_KEYS}ssh_host_ed25519_key" >> /etc/ssh/sshd_config && \
    sed -i "s/#PermitRootLogin.*/PermitRootLogin\ yes/" /etc/ssh/sshd_config && \
    echo "root:root" | chpasswd && \
    chmod a+x /usr/local/bin/* && \
    rm -rf /var/cache/apk/* /tmp/*

WORKDIR ${PROJECT_PATH}

#
# Saving dev virtualenv and ssh host keys
#
VOLUME ["${VENV_PATH}", "${SSH_SERVER_KEYS}"]

ENTRYPOINT ["entrypoint.sh"]

CMD ["/usr/sbin/sshd", "-D", "-e"]