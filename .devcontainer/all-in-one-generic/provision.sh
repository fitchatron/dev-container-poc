# setup permisison of ~/.ssh dir
sudo chown -R vscode:vscode ~/.ssh
sudo chmod -R 700 ~/.ssh

# make safe directory
git config --global --add safe.directory /workspace

# update packages
sudo apt-get update
sudo apt-get -y upgrade

# install unixODBC development headers
sudo apt-get install -y unixodbc-dev

# install pyodbc
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17

# install bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools17
echo 'export PATH="$PATH:/opt/mssql-tools17/bin"' >> ~/.bashrc
source ~/.bashrc

# install ansible
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible
