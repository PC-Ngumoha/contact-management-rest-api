# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer

    sudo apt-get update
    sudo apt-get install -y python3-venv zip

    BASH_ALIAS_PATH="/home/vagrant/.bash_aliases"
    touch "$BASH_ALIAS_PATH"
    
    if ! grep -q PYTHON_ALIAS_ADDED "$BASH_ALIAS_PATH"; then
      echo "# PYTHON_ALIAS_ADDED" >> "$BASH_ALIAS_PATH"
      echo "alias python='python3'" >> "$BASH_ALIAS_PATH"
    fi
  SHELL
end
